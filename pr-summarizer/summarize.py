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

def get_changed_files():
    event_path = os.environ.get('GITHUB_EVENT_PATH')
    if event_path and os.path.exists(event_path):
        with open(event_path, 'r') as f:
            event = json.load(f)
            # PR base SHA
            base_sha = event.get('pull_request', {}).get('base', {}).get('sha')
            if base_sha:
                return run_command(f"git diff --name-status {base_sha}...HEAD").split('\n')
    
    # Fallback to base ref or last commit
    base_ref = os.environ.get('GITHUB_BASE_REF', 'main')
    return run_command(f"git diff --name-status origin/{base_ref}...HEAD").split('\n')

def analyze_python(file_path):
    insights = []
    if not os.path.exists(file_path):
        return insights
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
    return list(set(insights)) # Unique

def analyze_gherkin(file_path):
    insights = []
    if not os.path.exists(file_path):
        return insights
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            scenarios = re.findall(r'Scenario: (.*)', content)
            for scenario in scenarios:
                insights.append(f"Scenario: `{scenario.strip()}`")
    except Exception as e:
        print(f"Warning: Could not analyze {file_path}: {e}")
    return list(set(insights))

def main():
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN not set.")
        return

    # Export GH_TOKEN for 'gh' CLI
    os.environ['GH_TOKEN'] = token

    target = os.environ.get('TARGET', 'description')
    
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
        
        if file_path.endswith('.py') and 'test' not in file_path.lower():
            technical_details.extend(analyze_python(file_path))
            change_types.add("♻️ **Refactor**" if status == 'M' else "✨ **New Feature**")
        elif file_path.endswith('.feature'):
            testing_plan.extend(analyze_gherkin(file_path))
            change_types.add("✨ **New Feature**")
        elif file_path.endswith('.css') or file_path.endswith('.tsx') or file_path.endswith('.jsx'):
            change_types.add("🎨 **Style/Design**")
        elif file_path.endswith('.md'):
            change_types.add("📚 **Documentation**")
        elif '.github/' in file_path:
            change_types.add("🔧 **Configuration**")

    if template_content:
        processed_body = template_content
        
        # 1. Select Change Types
        for ct in change_types:
            # Match both variations of checkboxes
            pattern = re.escape(f"- [ ] {ct}")
            processed_body = re.sub(pattern, f"- [x] {ct}", processed_body)

        # 2. Inject Technical Details
        if technical_details:
            details_str = "\n".join([f"- {d}" for d in technical_details[:10]])
            if "## 🛠️ Technical Details" in processed_body:
                # Use \g<1> to avoid digit ambiguity and lambda for escaping safety
                processed_body = re.sub(
                    r'(## 🛠️ Technical Details.*?\n)(?=-|\n)', 
                    lambda m: m.group(1) + details_str + '\n', 
                    processed_body, 
                    flags=re.DOTALL
                )

        # 3. Inject Testing Plan
        if testing_plan:
            tests_str = "\n".join([f"{i+1}. [x] {t}" for i, t in enumerate(testing_plan[:10])])
            if "## 🧪 Testing Plan" in processed_body:
                processed_body = re.sub(
                    r'(## 🧪 Testing Plan.*?\n)(?=1\.|-|\n)', 
                    lambda m: m.group(1) + tests_str + '\n', 
                    processed_body, 
                    flags=re.DOTALL
                )
        
        final_summary = processed_body
    else:
        # High-fidelity fallback
        final_summary = "### 🤖 Automated Technical Summary\n\n"
        final_summary += "#### 🌟 Predicted Change Types\n"
        for ct in change_types:
            final_summary += f"- [x] {ct}\n"
        final_summary += "\n#### 🛠️ Technical Insights\n"
        final_summary += "\n".join([f"- {detail}" for detail in technical_details[:10]]) if technical_details else "- Code pattern refinements."
        final_summary += "\n\n#### 🧪 Testing Scope\n"
        final_summary += "\n".join([f"- [x] {test}" for test in testing_plan[:10]]) if testing_plan else "- No new scenarios."

    with open('final_pr_body.md', 'w', encoding='utf-8') as f:
        f.write(final_summary)

    if target == 'description':
        print("Updating PR description via GitHub CLI...")
        # Check if we are in a PR
        pr_view = run_command("gh pr view --json number")
        if pr_view:
            run_command("gh pr edit --body-file final_pr_body.md")
        else:
            print("Not in a PR context or gh CLI error. Skipping edit.")
    else:
        print("Posting PR comment via GitHub CLI...")
        run_command("gh pr comment --body-file final_pr_body.md")

if __name__ == "__main__":
    main()
