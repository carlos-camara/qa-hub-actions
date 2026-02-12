import os
import json
import re
import subprocess
import ast
import fnmatch

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

def detect_file_purpose(file_path):
    """Intelligently detects the purpose of a file based on name and content."""
    name = file_path.lower()
    base = os.path.basename(name)
    
    # 1. Known Patterns
    if name.endswith('.py'): return "🐍 Python Logic"
    if name.endswith('.feature'): return "🧪 BDD Scenarios"
    if name.endswith(('.tsx', '.jsx', '.ts', '.js')) and any(x in name for x in ['component', 'view', 'page']): 
        return "⚛️ UI Component"
    if base == 'server.js' or base == 'app.js': return "🌐 Node.js Server/API"
    if 'docker-compose' in name: return "🔗 Docker Orchestration"
    if 'dockerfile' in name: return "🐳 Container Config"
    if name.endswith('.css'): return "🎨 UI Styling"
    if name.endswith('.yaml') and 'locators' in name: return "🎯 UI Locators"
    if name.endswith('.yaml') and 'config' in name: return "🔧 Configuration"
    if name.endswith('.sql'): return "🗄️ DB Migration"
    if name.endswith('.sh'): return "🐚 Shell Script"
    if name.endswith('.json'): return "📄 Data/Config"
    if name.endswith('.md'): return "📖 Documentation"
    
    # 2. Signature Check (if small enough)
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) < 10000:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(500).strip()
                if content.startswith('#!'): return "🐚 Executive Script"
                if 'FROM ' in content and 'RUN ' in content: return "🐳 Docker Image"
                if 'export ' in content: return "📦 JS Module"
    except: pass
    
    return "📄 Generic File"

def analyze_python(file_path, base_sha, status):
    insights = {"Structural": [], "API": [], "Breaking": []}
    if not os.path.exists(file_path):
        return insights
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                prefix = "[NEW]" if status == 'A' else "[MOD]"
                insights["Structural"].append(f"`{prefix}` `{node.name}`")
    except: pass

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            routes = re.findall(r'\.(get|post|put|delete|patch)\([\'"](/.+?)[\'"]', content)
            for method, path in routes:
                insights["API"].append(f"`{method.upper()}` `{path}`")
    except: pass

    diff = get_file_diff(file_path, base_sha)
    deleted_funcs = re.findall(r'^-def\s+(\w+)', diff, re.MULTILINE)
    for func in deleted_funcs:
        insights["Breaking"].append(f"🚨 `{func}` (Deleted)")

    return insights

def analyze_javascript(file_path, base_sha, status):
    insights = {"Structural": []}
    if not os.path.exists(file_path): return insights
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            exports = re.findall(r'export\s+(?:const|function|class)\s+(\w+)', content)
            for exp in exports:
                prefix = "[NEW]" if status == 'A' else "[MOD]"
                insights["Structural"].append(f"`{prefix}` `{exp}`")
    except: pass
    return insights

def analyze_gherkin(file_path, base_sha):
    insights, tags = [], []
    if not os.path.exists(file_path): return insights, tags
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            scenarios = re.findall(r'Scenario: (.*)', content)
            insights.extend([f"`{s.strip()}`" for s in scenarios])
            tags.extend(re.findall(r'@\w+', content))
    except: pass
    return insights, list(set(tags))

def calculate_risk(metrics, tech_insights):
    score = 0
    total_files = sum(metrics.values())
    if total_files > 15: score += 3
    elif total_files > 5: score += 1
    if tech_insights.get("Breaking"): score += 5
    if metrics.get("DevOps", 0) > 0: score += 2
    if score >= 5: return "🔴 **High Risk**"
    if score >= 2: return "🟡 **Medium Risk**"
    return "🟢 **Low Risk**"

def evaluate_intelligence(changed_files, metrics, tech_insights):
    flags, suggestions = [], []
    critical_files = [".env.template", "package.json", "qa_hub.db", "requirements.txt", "server.js"]
    doc_extensions = (".md", ".txt", ".yaml", ".yml")
    
    has_code_changes = any(metrics.get(k, 0) > 0 for k in ["Backend", "Frontend", "Logic", "App"])
    has_doc_changes = any(f.endswith(doc_extensions) for f in changed_files if "docs/" in f or f.endswith(".md"))
    
    for f in changed_files:
        if any(cf in f for cf in critical_files):
            flags.append(f"⚠️ **Core File Modified**: `{f}` detected.")
    
    if has_code_changes and not has_doc_changes:
        suggestions.append("📖 **Documentation Desync**: Consider updating `README.md` or adding documentation.")
    
    if tech_insights.get("Breaking"):
        flags.append("🚨 **Breaking Change**: Function deletions detected. Ensure downward compatibility.")

    return flags, suggestions

def main():
    token = os.environ.get('GITHUB_TOKEN')
    if not token: return
    os.environ['GH_TOKEN'] = token
    target = os.environ.get('TARGET', 'description')
    domain_mapping_raw = os.environ.get('DOMAIN_MAPPING', '{}')
    
    try:
        domain_mapping = json.loads(domain_mapping_raw)
    except:
        domain_mapping = {}

    event = get_event_data()
    pr_number = event.get('pull_request', {}).get('number')
    base_sha = event.get('pull_request', {}).get('base', {}).get('sha') or "HEAD~1"
    pr_title = event.get('pull_request', {}).get('title', "PR")

    template_path = ".github/pull_request_template.md"
    template_content = ""
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

    changed_files_raw = get_changed_files(event)
    if not changed_files_raw or changed_files_raw == ['']: return

    tech_insights = {"API Route": [], "Structural": [], "Locators": [], "Breaking": []}
    testing_plan, quality_tags, change_types = [], set(), set()
    metrics = {}
    file_intelligence = []

    for line in changed_files_raw:
        if not line: continue
        parts = line.split('\t')
        if len(parts) < 2: continue
        status, file_path = parts[0], parts[1]
        
        # 1. File Intelligence Breakdown
        purpose = detect_file_purpose(file_path)
        file_intelligence.append(f"- `{file_path}`: {purpose}")

        # 2. Categorization (Generic vs Default)
        matched_domain = None
        for domain, pattern in domain_mapping.items():
            if fnmatch.fnmatch(file_path, pattern):
                matched_domain = domain
                break
        
        if not matched_domain:
            if file_path.endswith('.py'): matched_domain = "Backend"
            elif file_path.endswith('.feature'): matched_domain = "QA"
            elif file_path.endswith(('.tsx', '.jsx', '.css')): matched_domain = "Frontend"
            elif '.github/' in file_path: matched_domain = "DevOps"
            else: matched_domain = "Other"
        
        metrics[matched_domain] = metrics.get(matched_domain, 0) + 1

        # 3. Deep Analysis
        if file_path.endswith('.py'):
            res = analyze_python(file_path, base_sha, status)
            tech_insights["API Route"].extend(res["API"])
            tech_insights["Structural"].extend(res["Structural"])
            tech_insights["Breaking"].extend(res["Breaking"])
            change_types.add("♻️ **Refactor**" if status == 'M' else "✨ **New Feature**")
        elif file_path.endswith('.feature'):
            scenarios, tags = analyze_gherkin(file_path, base_sha)
            testing_plan.extend(scenarios)
            quality_tags.update(tags)
            change_types.add("✨ **New Feature**")
        elif file_path.endswith(('.yaml', '.yml')) and ('locators' in file_path or 'config' in file_path):
            change_types.add("🔧 **Configuration**")
        elif file_path.endswith(('.tsx', '.jsx')):
            res = analyze_javascript(file_path, base_sha, status)
            tech_insights["Structural"].extend(res["Structural"])
            change_types.add("🎨 **Style/Design**")

    # Final Construction
    risk_level = calculate_risk(metrics, tech_insights)
    flags, suggestions = evaluate_intelligence([f.split('\t')[-1] for f in changed_files_raw if '\t' in f], metrics, tech_insights)

    # Building Markdown
    intel_str = f"## 🧠 Reviewer Intelligence\n"
    intel_str += f"**Risk Assessment**: {risk_level}\n\n"
    if flags:
        intel_str += "**Critical Flags**:\n"
        for flag in flags: intel_str += f"- {flag}\n"
        intel_str += "\n"
    
    # 📦 File Intelligence Section
    intel_str += "### 📦 File Intelligence Breakdown\n"
    for item in file_intelligence[:10]: intel_str += f"{item}\n"
    if len(file_intelligence) > 10: intel_str += f"- *...and {len(file_intelligence)-10} more files.*\n"
    intel_str += "\n"

    if suggestions:
        intel_str += "**Suggested Actions**:\n"
        for sugg in suggestions: intel_str += f"- {sugg}\n"
        intel_str += "\n"

    # technical details...
    details_str = ""
    for category, items in tech_insights.items():
        if items and category != "Breaking":
            details_str += f"\n**{category} Updates**\n"
            for item in list(set(items))[:5]: details_str += f"- {item}\n"

    if template_content:
        processed_body = template_content
        for ct in change_types: processed_body = re.sub(re.escape(f"- [ ] {ct}"), f"- [x] {ct}", processed_body)
        processed_body = re.sub(r'(## 🛠️ Technical Details.*?\n)(?=-|\n)', lambda m: m.group(1) + details_str + '\n', processed_body, flags=re.DOTALL)
        
        stats_table = "\n\n---\n### 📊 Impact Analysis\n"
        stats_table += "| Category | Scope | Bar |\n| :--- | :---: | :--- |\n"
        for k, v in metrics.items(): stats_table += f"| {k} | {v} | {'█' * min(v, 10)} |\n"
        final_summary = intel_str + "---\n" + processed_body + stats_table
    else:
        final_summary = f"### 🤖 Automated Summary for: {pr_title}\n" + intel_str + "\n---\n" + details_str

    with open('final_pr_body.md', 'w', encoding='utf-8') as f: f.write(final_summary)
    if pr_number:
        cmd = f"gh pr edit {pr_number} --body-file final_pr_body.md" if target == 'description' else f"gh pr comment {pr_number} --body-file final_pr_body.md"
        run_command(cmd)

if __name__ == "__main__": main()
