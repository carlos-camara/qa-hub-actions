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

def analyze_python(file_path, base_sha):
    insights = []
    breaking = []
    if not os.path.exists(file_path):
        return insights, breaking
    
    # Structural Insights
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                insights.append(f"Function: `{node.name}`")
            elif isinstance(node, ast.ClassDef):
                insights.append(f"Class: `{node.name}`")
    except: pass

    # API Footprint (Simplified)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            routes = re.findall(r'\.(get|post|put|delete|patch)\([\'"](/.+?)[\'"]', content)
            for method, path in routes:
                insights.append(f"API Route: `{method.upper()} {path}`")
    except: pass

    # Breaking Changes (AST Diffing placeholder)
    # If a file was modified, we'd ideally compare trees. Here we use diff markers.
    diff = get_file_diff(file_path, base_sha)
    deleted_funcs = re.findall(r'^-def\s+(\w+)', diff, re.MULTILINE)
    for func in deleted_funcs:
        breaking.append(f"Deleted Function: `{func}`")

    return list(set(insights)), list(set(breaking))

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
                insights.append(f"Scenario: `{scenario.strip()}`")
            
            # Extract tags
            all_tags = re.findall(r'@\w+', content)
            tags.extend(list(set(all_tags)))
    except: pass
    
    return list(set(insights)), list(set(tags))

def analyze_locators(file_path, base_sha):
    insights = []
    diff = get_file_diff(file_path, base_sha)
    # Detect changed keys in YAML-like files
    changed_keys = re.findall(r'^[+-]\s*(\w+):', diff, re.MULTILINE)
    for key in set(changed_keys):
        insights.append(f"Locator Update: `{key}`")
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

    technical_details = []
    testing_plan = []
    breaking_changes = []
    quality_tags = set()
    change_types = set()
    metrics = {"QA": 0, "Backend": 0, "Frontend": 0, "DevOps": 0, "Other": 0}

    for line in changed_files:
        if not line: continue
        parts = line.split('\t')
        if len(parts) < 2: continue
        status, file_path = parts[0], parts[1]
        
        # Metrics & Logic
        if file_path.endswith('.py'):
            insights, breaking = analyze_python(file_path, base_sha)
            technical_details.extend(insights)
            breaking_changes.extend(breaking)
            metrics["Backend"] += 1
            change_types.add("♻️ **Refactor**" if status == 'M' else "✨ **New Feature**")
        elif file_path.endswith('.feature'):
            scenarios, tags = analyze_gherkin(file_path, base_sha)
            testing_plan.extend(scenarios)
            quality_tags.update(tags)
            metrics["QA"] += 1
            change_types.add("✨ **New Feature**")
        elif file_path.endswith(('.yaml', '.yml')) and ('locators' in file_path or 'config' in file_path):
            technical_details.extend(analyze_locators(file_path, base_sha))
            metrics["QA"] += 1
            change_types.add("🔧 **Configuration**")
        elif file_path.endswith(('.tsx', '.jsx', '.css')):
            metrics["Frontend"] += 1
            change_types.add("🎨 **Style/Design**")
        elif '.github/' in file_path:
            metrics["DevOps"] += 1
            change_types.add("🔧 **Configuration**")

    # Construct Output
    if template_content:
        processed_body = template_content
        for ct in change_types:
            processed_body = re.sub(re.escape(f"- [ ] {ct}"), f"- [x] {ct}", processed_body)

        # Technical Details injection
        details_list = list(set(technical_details))[:15]
        if breaking_changes:
            details_list.insert(0, "⚠️ **BREAKING CHANGES DETECTED**")
            details_list.extend([f"🚨 {b}" for b in breaking_changes])
        
        if details_list:
            details_str = "\n".join([f"- {d}" for d in details_list])
            if "## 🛠️ Technical Details" in processed_body:
                processed_body = re.sub(r'(## 🛠️ Technical Details.*?\n)(?=-|\n)', lambda m: m.group(1) + details_str + '\n', processed_body, flags=re.DOTALL)

        # Testing Plan injection
        if testing_plan:
            tests_str = "\n".join([f"{i+1}. [x] {t}" for i, t in enumerate(testing_plan[:10])])
            if quality_tags:
                tests_str += f"\n\n**Tags Context**: {', '.join(quality_tags)}"
            if "## 🧪 Testing Plan" in processed_body:
                processed_body = re.sub(r'(## 🧪 Testing Plan.*?\n)(?=1\.|-|\n)', lambda m: m.group(1) + tests_str + '\n', processed_body, flags=re.DOTALL)
        
        # Add Metrics at the end
        stats = "\n\n---\n### 📊 Change Metrics\n"
        stats += " | ".join([f"**{k}**: {v}" for k, v in metrics.items() if v > 0])
        final_summary = processed_body + stats
    else:
        final_summary = "### 🤖 Automated Technical Summary\n"
        # ... Fallback (similar structure)

    with open('final_pr_body.md', 'w', encoding='utf-8') as f:
        f.write(final_summary)

    if pr_number:
        cmd = f"gh pr edit {pr_number} --body-file final_pr_body.md" if target == 'description' else f"gh pr comment {pr_number} --body-file final_pr_body.md"
        run_command(cmd)

if __name__ == "__main__":
    main()
