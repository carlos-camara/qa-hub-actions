import os
import json
import re
import subprocess
import ast

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e.stderr}")
        return ""

def get_event_data():
    event_path = os.environ.get('GITHUB_EVENT_PATH')
    if event_path and os.path.exists(event_path):
        with open(event_path, 'r') as f:
            return json.load(f)
    return {}

def get_changed_files(event):
    base_sha = event.get('pull_request', {}).get('base', {}).get('sha')
    if base_sha:
        return run_command(f"git diff --name-status {base_sha}...HEAD").split('\n')
    base_ref = os.environ.get('GITHUB_BASE_REF', 'main')
    return run_command(f"git diff --name-status origin/{base_ref}...HEAD").split('\n')

def get_file_diff(file_path, base_sha):
    return run_command(f"git diff -U0 {base_sha}...HEAD -- {file_path}")

def analyze_python(file_path, base_sha, status):
    insights = {"Structural": [], "API": [], "Breaking": []}
    if not os.path.exists(file_path):
        return insights
    
    label = "  " if status == 'M' else "✨ "
    
    # Structural Insights
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                prefix = "[NEW]" if status == 'A' else "[MOD]"
                insights["Structural"].append(f"`{prefix}` `{node.name}`")
            elif isinstance(node, ast.ClassDef):
                prefix = "[NEW]" if status == 'A' else "[MOD]"
                insights["Structural"].append(f"`{prefix}` `{node.name}`")
    except: pass

    # API Footprint
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            routes = re.findall(r'\.(get|post|put|delete|patch)\([\'"](/.+?)[\'"]', content)
            for method, path in routes:
                insights["API"].append(f"`{method.upper()}` `{path}`")
    except: pass

    # Breaking Changes
    diff = get_file_diff(file_path, base_sha)
    deleted_funcs = re.findall(r'^-def\s+(\w+)', diff, re.MULTILINE)
    for func in deleted_funcs:
        insights["Breaking"].append(f"🚨 `{func}` (Deleted)")

    return insights

def analyze_gherkin(file_path, base_sha):
    insights = []
    tags = []
    if not os.path.exists(file_path):
        return insights, tags
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            scenarios = re.findall(r'Scenario: (.*)', content)
            for scenario in scenarios:
                insights.append(f"`{scenario.strip()}`")
            all_tags = re.findall(r'@\w+', content)
            tags.extend(list(set(all_tags)))
    except: pass
    return insights, list(set(tags))

def analyze_locators(file_path, base_sha):
    insights = []
    diff = get_file_diff(file_path, base_sha)
    adds = re.findall(r'^\+\s*(\w+):', diff, re.MULTILINE)
    mods = re.findall(r'^-\s*(\w+):', diff, re.MULTILINE)
    
    for key in set(adds):
        insights.append(f"`[NEW]` `{key}`")
    for key in set(mods):
        if key not in set(adds): # Only if not replaced in the same diff
            insights.append(f"`[MOD]` `{key}`")
    return insights

def main():
    token = os.environ.get('GITHUB_TOKEN')
    if not token: return
    os.environ['GH_TOKEN'] = token
    target = os.environ.get('TARGET', 'description')
    
    event = get_event_data()
    pr_number = event.get('pull_request', {}).get('number')
    base_sha = event.get('pull_request', {}).get('base', {}).get('sha') or "HEAD~1"

    template_path = ".github/pull_request_template.md"
    template_content = ""
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

    changed_files = get_changed_files(event)
    if not changed_files or changed_files == ['']: return

    tech_insights = {"API Route": [], "Structural": [], "Locators": [], "Breaking": []}
    testing_plan = []
    quality_tags = set()
    change_types = set()
    metrics = {"QA": 0, "Backend": 0, "Frontend": 0, "DevOps": 0}

    for line in changed_files:
        if not line: continue
        parts = line.split('\t')
        if len(parts) < 2: continue
        status, file_path = parts[0], parts[1]
        
        if file_path.endswith('.py'):
            res = analyze_python(file_path, base_sha, status)
            tech_insights["API Route"].extend(res["API"])
            tech_insights["Structural"].extend(res["Structural"])
            tech_insights["Breaking"].extend(res["Breaking"])
            metrics["Backend"] += 1
            change_types.add("♻️ **Refactor**" if status == 'M' else "✨ **New Feature**")
        elif file_path.endswith('.feature'):
            scenarios, tags = analyze_gherkin(file_path, base_sha)
            testing_plan.extend(scenarios)
            quality_tags.update(tags)
            metrics["QA"] += 1
            change_types.add("✨ **New Feature**")
        elif file_path.endswith(('.yaml', '.yml')) and ('locators' in file_path or 'config' in file_path):
            tech_insights["Locators"].extend(analyze_locators(file_path, base_sha))
            metrics["QA"] += 1
            change_types.add("🔧 **Configuration**")
        elif file_path.endswith(('.tsx', '.jsx', '.css')):
            metrics["Frontend"] += 1
            change_types.add("🎨 **Style/Design**")
        elif '.github/' in file_path:
            metrics["DevOps"] += 1
            change_types.add("🔧 **Configuration**")

    # Format Technical Details (Grouped and Pretty)
    details_str = ""
    # 1. API Changes
    if tech_insights["API Route"]:
        details_str += "\n**🌐 API Footprint**\n"
        for item in list(set(tech_insights["API Route"]))[:5]:
            details_str += f"- {item}\n"
    # 2. Structural Changes
    if tech_insights["Structural"]:
        details_str += "\n**🏗️ Structural Impact**\n"
        for item in list(set(tech_insights["Structural"]))[:5]:
            details_str += f"- {item}\n"
    # 3. Locators
    if tech_insights["Locators"]:
        details_str += "\n**🎯 Locator Updates**\n"
        for item in list(set(tech_insights["Locators"]))[:5]:
            details_str += f"- {item}\n"
    # 4. Breaking
    if tech_insights["Breaking"]:
        details_str += "\n> [!CAUTION]\n"
        details_str += "> **Potential Breaking Changes Detected**\n"
        for item in list(set(tech_insights["Breaking"])):
            details_str += f"> - {item}\n"

    # Construct Output
    if template_content:
        processed_body = template_content
        for ct in change_types:
            processed_body = re.sub(re.escape(f"- [ ] {ct}"), f"- [x] {ct}", processed_body)

        # Injection
        if details_str:
            processed_body = re.sub(r'(## 🛠️ Technical Details.*?\n)(?=-|\n)', lambda m: m.group(1) + details_str + '\n', processed_body, flags=re.DOTALL)

        if testing_plan:
            tests_str = "\n".join([f"{i+1}. [x] {t}" for i, t in enumerate(testing_plan[:10])])
            if quality_tags:
                tests_str += f"\n\n> [!NOTE]\n> **Context Tags**: {', '.join(quality_tags)}"
            processed_body = re.sub(r'(## 🧪 Testing Plan.*?\n)(?=1\.|-|\n)', lambda m: m.group(1) + tests_str + '\n', processed_body, flags=re.DOTALL)
        
        # Metrics Table
        stats_table = "\n\n---\n### 📊 Impact Analysis\n\n"
        stats_table += "| Category | Scope | Status |\n"
        stats_table += "| :--- | :---: | :--- |\n"
        for k, v in metrics.items():
            if v > 0:
                bar = "█" * min(v, 10)
                stats_table += f"| {k} | {v} | {bar} |\n"
        
        final_summary = processed_body + stats_table
    else:
        final_summary = "### 🤖 Automated Technical Summary\n" + details_str

    with open('final_pr_body.md', 'w', encoding='utf-8') as f:
        f.write(final_summary)

    if pr_number:
        cmd = f"gh pr edit {pr_number} --body-file final_pr_body.md" if target == 'description' else f"gh pr comment {pr_number} --body-file final_pr_body.md"
        run_command(cmd)

if __name__ == "__main__":
    main()
