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
    
    return "📦 Miscellaneous"

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

        # 2. Categorization
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
            else: matched_domain = "📦 Miscellaneous"
        
        metrics[matched_domain] = metrics.get(matched_domain, 0) + 1

        # 3. Deep Analysis
        if file_path.endswith('.py'):
            res = analyze_python(file_path, base_sha, status)
            tech_insights["API Route"].extend(res["API"])
            tech_insights["Structural"].extend(res["Structural"])
            tech_insights["Breaking"].extend(res["Breaking"])
            change_types.add("♻️ **Refactor**" if status == 'M' else "🚀 **New Feature**")
        elif file_path.endswith('.feature'):
            scenarios, tags = analyze_gherkin(file_path, base_sha)
            testing_plan.extend(scenarios)
            quality_tags.update(tags)
            change_types.add("🚀 **New Feature**")
        elif file_path.endswith(('.yaml', '.yml')) and ('locators' in file_path or 'config' in file_path):
            change_types.add("🔧 **Configuration**")
        elif file_path.endswith(('.tsx', '.jsx')):
            res = analyze_javascript(file_path, base_sha, status)
            tech_insights["Structural"].extend(res["Structural"])
            change_types.add("💄 **UI/UX**")
        elif file_path.endswith('.md'):
            change_types.add("📚 **Documentation**")
        elif 'security' in file_path.lower():
            change_types.add("🛡️ **Security**")

    # High-Fidelity Construction
    flags, suggestions = evaluate_intelligence([f.split('\t')[-1] for f in changed_files_raw if '\t' in f], metrics, tech_insights)
    
    # Unified Risk Calculation
    score = 0
    total_files = sum(metrics.values())
    if total_files > 15: score += 3
    elif total_files > 5: score += 1
    if tech_insights.get("Breaking"): score += 5
    if metrics.get("DevOps", 0) > 0: score += 2
    if flags: score += 5 # Force High Risk if critical flags exist

    if score >= 5: risk_lvl, risk_color = "🔴 High Risk", "CAUTION"
    elif score >= 2: risk_lvl, risk_color = "🟡 Medium Risk", "IMPORTANT"
    else: risk_lvl, risk_color = "🟢 Low Risk", "NOTE"

    # --- 1. Strategic Dashboard (Executive Summary) ---
    effort = "Quick" if total_files < 5 else "Balanced" if total_files < 15 else "Heavy"
    complexity = "Modular" if not tech_insights.get("Breaking") else "High"
    effort_icon = "⚡" if total_files < 5 else "⚖️" if total_files < 15 else "🏋️"
    complexity_icon = "🧩" if not tech_insights.get("Breaking") else "💥"
    
    # High-impact summary sentence
    summary_msg = f"This PR executes a **{', '.join([c.split(' ')[1].replace('**', '') for c in change_types if '**' in c] or ['Core'])}** update across **{len(metrics)}** architectural layers."

    intel_str = f"> [!{risk_color}]\n"
    intel_str += f"> > {summary_msg}\n"
    intel_str += f"> \n"
    intel_str += f"> | IMPACT | TIMELINE | STRUCTURAL |\n"
    intel_str += f"> | :--- | :--- | :--- |\n"
    intel_str += f"> | {risk_lvl.replace('Risk', '').strip()} | **{effort_icon} {effort}** | **{complexity_icon} {complexity}** |\n"
    intel_str += f"> \n"
    
    if flags or suggestions:
        intel_str += f"> --- \n"
        intel_str += f"> \n"
        intel_str += f"> ### 🚩 KEY FINDINGS\n"
        for f in flags: 
            f_clean = f.replace("⚠️ ", "").replace("🚨 ", "")
            intel_str += f"> - `[CRITICAL]` {f_clean}\n"
        for s in suggestions:
            s_clean = s.replace("📖 ", "").replace("🛡️ ", "")
            intel_str += f"> - `[ADVISORY]` {s_clean}\n"
    
    intel_str += "\n"

    # --- 2. Components Inventory (Collapsible) ---
    status_map = {"A": "🟢 NEW", "M": "🔵 MOD", "D": "🔴 DEL", "R": "🟡 REN"}
    inventory_str = "### 📦 Components Inventory\n"
    grouped_files = {}
    for line in changed_files_raw:
        if not line: continue
        parts = line.split('\t')
        if len(parts) < 2: continue
        s, f = parts[0], parts[1]
        p = detect_file_purpose(f)
        if p not in grouped_files: grouped_files[p] = []
        grouped_files[p].append((s, f))
    
    for p in sorted(grouped_files.keys()):
        files = grouped_files[p]
        inventory_str += f"<details><summary><b>{p} ({len(files)})</b></summary>\n\n"
        for s, f in files[:10]:
            st = status_map.get(s[0], "🔵 MOD")
            inventory_str += f"- ` {st} ` `{f}`\n"
        if len(files) > 10: inventory_str += f"- *... and {len(files) - 10} more*\n"
        inventory_str += "\n</details>"
    inventory_str += "\n\n"

    # --- 3. High-Priority Review Focus ---
    focus_str = ""
    focus_files = [f.split('\t')[-1] for f in changed_files_raw if '\t' in f]
    top_focus = [f for f in focus_files if any(p in f for p in ["server.js", "db.js", "App.tsx", ".yml"]) or "workflows/" in f]
    if top_focus:
        focus_str += "### 🎯 High-Priority Review Focus\n"
        for f in top_focus[:3]: focus_str += f"- [ ] `{f}` (Core System Change)\n"
        focus_str += "\n"

    # Final Intel Assembly
    intel_str = f"{intel_str}{inventory_str}{focus_str}"

    # --- 2. Template Integration ---
    # --- 2. Template Integration ---
    if template_content:
        # 2.1 Change Classification Auto-Detection
        title_map = {
            "feat": "🚀 **PROD-FEATURE**", 
            "fix": "🐛 **HOTFIX**", 
            "refactor": "♻️ **REFACTOR**", 
            "style": "💄 **STYLING**", 
            "docs": "🔧 **INFRA**", 
            "chore": "🔧 **INFRA**", 
            "perf": "⚡ **PERF-BOOST**"
        }
        
        pr_type_match = re.search(r'^(feat|fix|refactor|style|docs|chore|perf)', pr_title.lower())
        if pr_type_match:
            detected_class = title_map.get(pr_type_match.group(1))
            if detected_class: change_types.add(detected_class)
        
        if risk_lvl == "🔴 High Risk": change_types.add("💥 **BREAKING**")

        processed_body = template_content
        processed_body = processed_body.replace("[Brief Title]", pr_title)
        
        # 2.2 Dashboard Highlighting
        for cls in change_types:
            pattern = rf"\| \[ \] \| {re.escape(cls)}"
            processed_body = re.sub(pattern, f"| ✅ | {cls}", processed_body)

        # 2.3 Intelligence Delivery (Executive Summary)
        summary_anchor = "# 🌟 Executive Summary"
        if summary_anchor in processed_body:
            pattern = rf"({re.escape(summary_anchor)}\n(?:<!--.*?-->\n)?)>[ \t]*.*?\n"
            processed_body = re.sub(pattern, rf"\1\n{intel_str}", processed_body, flags=re.DOTALL)
        else:
            processed_body = f"{intel_str}\n{processed_body}"

        # 2.4 Evidence Delivery (Change Magnitude Stats)
        evidence_anchor = "## ✅ Verification Evidence"
        total_files = sum(metrics.values())
        stats_table = "\n### 📊 Change Magnitude & Distribution\n"
        stats_table += "| Layer | Units | % | Magnitude |\n| :--- | :---: | :---: | :--- |\n"
        layer_icons = {"Frontend": "🎨", "Backend": "⚙️", "QA": "🧪", "DevOps": "🚀", "📦 Miscellaneous": "📦"}

        for k, v in sorted(metrics.items(), key=lambda x: x[1], reverse=True):
            pct = (v / total_files * 100) if total_files > 0 else 0
            icon = layer_icons.get(k, "📄")
            filled_count = min(round(pct / 10), 10)
            bar = '▰' * filled_count + '▱' * (10 - filled_count)
            stats_table += f"| {icon} {k} | {v} | {pct:.1f}% | `{bar}` |\n"

        if evidence_anchor in processed_body:
            pattern = rf"({re.escape(evidence_anchor)}\n(?:<!--.*?-->\n)?)"
            processed_body = re.sub(pattern, rf"\1{stats_table}\n", processed_body, flags=re.DOTALL)
        else:
            processed_body = f"{processed_body}\n{stats_table}"

        processed_body = re.sub(r'<!--.*?-->', '', processed_body, flags=re.DOTALL)
        processed_body = processed_body.replace("_[Drop screenshot/video here]_", "*(Automated: No attachments detected)*")
        final_summary = processed_body
    else:
        final_summary = f"{intel_str}\n---\n*Manual review required: No PR template found.*"

    with open('final_pr_body.md', 'w', encoding='utf-8') as f: f.write(final_summary)
    if pr_number:
        cmd = f"gh pr edit {pr_number} --body-file final_pr_body.md" if target == 'description' else f"gh pr comment {pr_number} --body-file final_pr_body.md"
        run_command(cmd)

if __name__ == "__main__": main()
