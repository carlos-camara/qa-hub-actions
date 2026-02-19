import os
import json
import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e.stderr}")
        return ""

def main():
    token = os.environ.get('GH_TOKEN')
    if not token:
        print("❌ GH_TOKEN not found.")
        sys.exit(1)

    event_path = os.environ.get('EVENT_PATH')
    with open(event_path, 'r') as f:
        event = json.load(f)

    pr = event.get('pull_request')
    if not pr:
        return

    pr_number = pr['number']
    pr_body = pr.get('body', '')
    repo = os.environ.get('REPO_FULL_NAME')
    base_ref = os.environ.get('GITHUB_BASE_REF', 'main')
    
    logic_path = os.environ.get('LOGIC_PATH')
    test_path = os.environ.get('TEST_PATH')
    debt_logic_limit = int(os.environ.get('DEBT_LOGIC', 50))
    debt_test_min = int(os.environ.get('DEBT_TESTS', 5))

    print(f"📈 Analyzing Churn (Logic: {logic_path}, Tests: {test_path})...")
    
    # Calculate Logic Stats
    logic_stats = run_command(f"git diff --numstat origin/{base_ref}...HEAD | grep '{logic_path}' || echo '0 0'")
    logic_add = sum([int(line.split()[0]) for line in logic_stats.split('\n') if line])
    logic_del = sum([int(line.split()[1]) for line in logic_stats.split('\n') if line])

    # Calculate Test Stats
    test_stats = run_command(f"git diff --numstat origin/{base_ref}...HEAD | grep '{test_path}' || echo '0 0'")
    test_add = sum([int(line.split()[0]) for line in test_stats.split('\n') if line])
    test_del = sum([int(line.split()[1]) for line in test_stats.split('\n') if line])

    print(f"Logic: +{logic_add} / -{logic_del}")
    print(f"Tests: +{test_add} / -{test_del}")

    debt_found = False
    debt_msg = ""

    # 1. Significant Test Deletion
    if test_del > (test_add + 5):
        debt_found = True
        debt_msg = f"⚠️ **Significant Test Deletion**: More tests are being removed than added (-{test_del - test_add} lines)."
    
    # 2. Feature Churn without tests
    if logic_add > debt_logic_limit and test_add < debt_test_min:
        debt_found = True
        debt_msg = f"⚠️ **Feature Churn**: Large logic change ({logic_add}+ lines) detected with minimal test updates ({test_add} lines)."

    if debt_found:
        print(f"🚨 {debt_msg}")
        run_command(f'gh label create "quality/test-debt" --color "E99695" --description "Negative test/logic balance" --repo {repo} --force || true')
        run_command(f'gh pr edit {pr_number} --add-label "quality/test-debt" --repo {repo}')
        
        # Inject Warning
        report = f"> [!WARNING]\\n> ### 📉 QUALITY METRICS ALERT\\n> {debt_msg}\\n>\\n"
        report += f"> | Component | Added | Deleted |\\n> | :--- | :--- | :--- |\\n"
        report += f"> | ⚙️ Logic | {logic_add} | {logic_del} |\\n> | 🧪 Tests | {test_add} | {test_del} |\\n---\\\\n"
        
        if "QUALITY METRICS ALERT" not in pr_body:
            new_body = report + pr_body
            with open('debt_body.md', 'w', encoding='utf-8') as f_db:
                f_db.write(new_body)
            run_command(f'gh pr edit {pr_number} --body-file debt_body.md --repo {repo}')
    else:
        print("✅ Healthy test/logic balance.")
        # Remove label if present
        current_labels = run_command(f'gh pr view {pr_number} --json labels --template "{{{{range .labels}}}}{{{{ .name }}}} {{{{end}}}}" --repo {repo}')
        if "quality/test-debt" in current_labels:
            run_command(f'gh pr edit {pr_number} --remove-label "quality/test-debt" --repo {repo}')

if __name__ == "__main__":
    main()
