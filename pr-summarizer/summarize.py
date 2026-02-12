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
    # Get changed files in PR
    base_sha = os.environ.get('GITHUB_BASE_REF', 'main')
    head_sha = os.environ.get('GITHUB_HEAD_REF', '')
    
    if head_sha:
        # In PR context, diff against base branch
        return run_command(f"git diff --name-status origin/{base_sha}...HEAD").split('\n')
    else:
        # Fallback to last commit if not in PR
        return run_command("git diff --name-status HEAD~1 HEAD").split('\n')

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
    target = os.environ.get('TARGET', 'description')
    mapping_str = os.environ.get('DOMAIN_MAPPING', '{}')
    
    try:
        mapping = json.loads(mapping_str)
    except:
        mapping = {}

    default_mapping = {
        'Frontend': ['.tsx', '.jsx', '.css', '.html'],
        'Backend': ['server.js', 'services/', '.py'],
        'QA/Automation': ['.feature', 'steps/', 'locators/'],
        'DevOps': ['.github/', 'docker/']
    }
    
    # Merge mappings
    active_mapping = default_mapping.copy()
    active_mapping.update(mapping)

    changed_files = get_changed_files()
    if not changed_files or changed_files == ['']:
        print("No changes detected.")
        return

    domain_changes = {domain: [] for domain in active_mapping.keys()}
    domain_changes['Other'] = []
    
    technical_details = []
    testing_plan = []
    change_types = set()

    for line in changed_files:
        if not line: continue
        parts = line.split('\t')
        if len(parts) < 2: continue
        status, file_path = parts[0], parts[1]
        
        # Categorize
        found_domain = False
        for domain, patterns in active_mapping.items():
            if any(pattern in file_path for pattern in patterns):
                domain_changes[domain].append(file_path)
                found_domain = True
                break
        if not found_domain:
            domain_changes['Other'].append(file_path)

        # Deep Analysis
        if file_path.endswith('.py') and 'test' not in file_path.lower():
            technical_details.extend(analyze_python(file_path))
            change_types.add("Refactor" if status == 'M' else "New Feature")
        elif file_path.endswith('.feature'):
            scenarios = analyze_gherkin(file_path)
            testing_plan.extend(scenarios)
            change_types.add("New Feature")
        elif file_path.endswith('.css') or file_path.endswith('.tsx'):
            change_types.add("Style/Design")

    # Load Template
    template_path = ".github/pull_request_template.md"
    template_content = ""
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

    # Construct Summary
    summary = "### 🤖 Automated Technical Summary\n\n"
    
    summary += "#### 🌟 Predicted Change Types\n"
    for ct in change_types:
        summary += f"- [x] {ct}\n"
    summary += "\n"

    summary += "#### 🛠️ Technical Insights\n"
    if technical_details:
        for detail in technical_details[:10]: # Cap it
            summary += f"- {detail}\n"
    else:
        summary += "- Internal logic updates and architectural refinements.\n"
    summary += "\n"

    summary += "#### 🧪 Automated Testing Scope\n"
    if testing_plan:
        for test in testing_plan:
            summary += f"- [x] {test}\n"
    else:
        summary += "- No new Gherkin scenarios detected.\n"
    summary += "\n"

    summary += "#### 📂 Domain Impact\n"
    for domain, files in domain_changes.items():
        if files:
            summary += f"- **{domain}**: {len(files)} files modified\n"

    # Post Summary
    print(summary)
    
    # In a real environment, we'd use 'gh pr edit' or 'gh pr comment'
    # For now, we write to a file that the composite action can use or just print it.
    with open('pr_summary.md', 'w', encoding='utf-8') as f:
        f.write(summary)

if __name__ == "__main__":
    main()
