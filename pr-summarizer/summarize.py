import os
import json
import re
import subprocess
import ast

def run_command(command):
    try:
        # Use shell=True for complex commands with pipes/redirects
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e.stderr}")
        return ""

def get_changed_files():
    # In GitHub Actions, we usually have access to the event payload
    event_path = os.environ.get('GITHUB_EVENT_PATH')
    if event_path and os.path.exists(event_path):
        with open(event_path, 'r') as f:
            event = json.load(f)
            # For pull_request events, we can get the base/head from here or just use git
            base_sha = event.get('pull_request', {}).get('base', {}).get('sha', 'main')
            return run_command(f"git diff --name-status {base_sha}...HEAD").split('\n')
    
    # Fallback
    base_ref = os.environ.get('GITHUB_BASE_REF', 'main')
    return run_command(f"git diff --name-status origin/{base_ref}...HEAD").split('\n')

def analyze_python(file_path):
    insights = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                insights.append(f"Function: `{node.name}`")
            elif isinstance(node, ast.ClassDef):
                insights.append(f"Class: `{node.name}`")
    except Exception as e:
        print(f"Warning: Could not analyze {file_path}: {e}")
    return insights

def analyze_gherkin(file_path):
    insights = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            scenarios = re.findall(r'Scenario: (.*)', content)
            for scenario in scenarios:
                insights.append(f"Scenario: `{scenario.strip()}`")
    except Exception as e:
        print(f"Warning: Could not analyze {file_path}: {e}")
    return insights

def main():
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN not set.")
        return

    target = os.environ.get('TARGET', 'description')
    
    # Load Template
    template_path = ".github/pull_request_template.md"
    template_content = ""
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

    changed_files = get_changed_files()
    if not changed_files or changed_files == ['']:
        print("No changes detected.")
        return

    technical_details = []
    testing_plan = []
    change_types = set()

    for line in changed_files:
        if not line: continue
        parts = line.split('\t')
        if len(parts) < 2: continue
        status, file_path = parts[0], parts[1]
        
        # Deep Analysis
        if file_path.endswith('.py') and 'test' not in file_path.lower():
            technical_details.extend(analyze_python(file_path))
            change_types.add("♻️ **Refactor**" if status == 'M' else "✨ **New Feature**")
        elif file_path.endswith('.feature'):
            scenarios = analyze_gherkin(file_path)
            testing_plan.extend(scenarios)
            change_types.add("✨ **New Feature**")
        elif file_path.endswith('.css') or file_path.endswith('.tsx'):
            change_types.add("🎨 **Style/Design**")
        elif file_path.endswith('.md'):
            change_types.add("📚 **Documentation**")

    # If we have a template, let's try to populate it
    if template_content:
        processed_body = template_content
        
        # 1. Select Change Types
        for ct in change_types:
            # Look for "- [ ] **Refactor**" etc and check it
            # Escaping for regex
            pattern = re.escape(f"- [ ] {ct}")
            processed_body = re.sub(pattern, f"- [x] {ct}", processed_body)

        # 2. Inject Technical Details
        if technical_details:
            details_str = "\n".join([f"- {d}" for d in technical_details[:10]])
            # Look for the section after ## 🛠️ Technical Details
            processed_body = re.sub(r'(## 🛠️ Technical Details.*?\n)- ', r'\1' + details_str + '\n- ', processed_body, flags=re.DOTALL)

        # 3. Inject Testing Plan
        if testing_plan:
            tests_str = "\n".join([f"{i+1}. [x] {t}" for i, t in enumerate(testing_plan[:10])])
            processed_body = re.sub(r'(## 🧪 Testing Plan.*?\n)1\.', r'\1' + tests_str + '\n1.', processed_body, flags=re.DOTALL)
        
        final_summary = processed_body
    else:
        # Fallback summary
        final_summary = "### 🤖 Automated Technical Summary\n\n"
        final_summary += "#### 🌟 Predicted Change Types\n"
        for ct in change_types:
            final_summary += f"- [x] {ct}\n"
        final_summary += "\n#### 🛠️ Technical Insights\n"
        final_summary += "\n".join([f"- {d}" for d in technical_details[:10]]) or "- Internal refinements."
        final_summary += "\n\n#### 🧪 Testing Scope\n"
        final_summary += "\n".join([f"- [x] {t}" for t in testing_plan[:10]]) or "- No new scenarios."

    # Perform the update
    with open('final_pr_body.md', 'w', encoding='utf-8') as f:
        f.write(final_summary)

    if target == 'description':
        print("Updating PR description...")
        run_command("gh pr edit --body-file final_pr_body.md")
    else:
        print("Posting PR comment...")
        run_command("gh pr comment --body-file final_pr_body.md")

if __name__ == "__main__":
    main()
