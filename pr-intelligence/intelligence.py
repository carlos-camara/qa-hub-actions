import os
import json
import re
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
        print("⏭️ Not a Pull Request event. Skipping.")
        return

    pr_number = pr['number']
    pr_title = pr['title']
    pr_body = pr.get('body', '')
    repo = os.environ.get('REPO_FULL_NAME')
    base_ref = os.environ.get('GITHUB_BASE_REF', 'main')

    # 1. Hygiene Validation
    if os.environ.get('VALIDATE_HYGIENE') == 'true':
        print("📝 Validating PR Hygiene...")
        # Conventional Commits Regex
        regex = r'^(feat|fix|chore|docs|style|refactor|test|perf)(\(.*\))?!?: .+$'
        if not re.match(regex, pr_title):
            msg = "❌ **Invalid PR Title**: Please use [Conventional Commits](https://www.conventionalcommits.org/)."
            run_command(f'gh pr comment {pr_number} --body "{msg}" --repo {repo}')
            print(f"Hygiene Failed: {msg}")
            sys.exit(1)
        
        if not pr_body or len(pr_body) < 15:
            msg = "❌ **Incomplete Description**: Please provide a detailed description (>15 characters)."
            run_command(f'gh pr comment {pr_number} --body "{msg}" --repo {repo}')
            print(f"Hygiene Failed: {msg}")
            sys.exit(1)
        print("✅ Hygiene passed.")

    # 2. Size Labeling
    if os.environ.get('LABEL_SIZE') == 'true':
        print("📏 Calculating PR Size...")
        diff_stat = run_command(f"git diff --shortstat origin/{base_ref}...HEAD")
        # Example: 2 files changed, 150 insertions(+), 10 deletions(-)
        match = re.search(r'(\d+) insertions\(\+\), (\d+) deletions\(-\)', diff_stat)
        if match:
            lines = int(match.group(1)) + int(match.group(2))
        else:
            # Fallback for small diffs where maybe only one of them exists
            match_ins = re.search(r'(\d+) insertion', diff_stat)
            match_del = re.search(r'(\d+) deletion', diff_stat)
            lines = (int(match_ins.group(1)) if match_ins else 0) + (int(match_del.group(1)) if match_del else 0)

        print(f"Lines changed: {lines}")
        
        if lines < 50: size = "size/S"; color = "0E8A16"; desc = "Quick review (< 50 lines)"
        elif lines < 200: size = "size/M"; color = "FBCA04"; desc = "Standard review (50-200 lines)"
        elif lines < 500: size = "size/L"; color = "EB6420"; desc = "Deep review (200-500 lines)"
        else: size = "size/XL"; color = "D93F0B"; desc = "Significant change (> 500 lines)"

        # Ensure labels exist
        run_command(f'gh label create "{size}" --color "{color}" --description "{desc}" --repo {repo} --force || true')
        
        # Get current labels
        current_labels = run_command(f'gh pr view {pr_number} --json labels --template "{{{{range .labels}}}}{{{{ .name }}}} {{{{end}}}}" --repo {repo}')
        
        # Add label if missing
        if size not in current_labels:
            # Remove other size labels
            for l in ["size/S", "size/M", "size/L", "size/XL"]:
                if l in current_labels and l != size:
                    run_command(f'gh pr edit {pr_number} --remove-label "{l}" --repo {repo}')
            run_command(f'gh pr edit {pr_number} --add-label "{size}" --repo {repo}')
            print(f"✅ Applied {size}")

    # 3. Risk Analysis
    if os.environ.get('ANALYZE_RISK') == 'true':
        print("🤖 Analyzing Risk...")
        patterns = os.environ.get('CRITICAL_PATTERNS', '').split(',')
        changed_files = run_command(f"git diff --name-only origin/{base_ref}...HEAD").split('\n')
        
        risk_files = []
        for f in changed_files:
            for p in patterns:
                if p and p in f:
                    risk_files.append(f)
                    break
        
        if risk_files:
            print(f"⚠️ {len(risk_files)} critical files modified.")
            run_command(f'gh label create "high-risk" --color "B60205" --description "Critical files modified" --repo {repo} --force || true')
            run_command(f'gh pr edit {pr_number} --add-label "high-risk" --repo {repo}')
            
            # Inject Warning in Body
            matched_msg = "\n".join([f"- `{f}`" for f in risk_files])
            warning = f"> [!CAUTION]\\n> ### ⚠️ HIGH RISK CHANGE DETECTED\\n> This PR modifies critical files:\\n{matched_msg}\\n---\\n"
            
            if "!CAUTION" not in pr_body:
                new_body = warning + pr_body
                with open('new_body.md', 'w', encoding='utf-8') as f_wb:
                    f_wb.write(new_body)
                run_command(f'gh pr edit {pr_number} --body-file new_body.md --repo {repo}')
                print("✅ Risk warning injected.")
        else:
            print("🟢 No critical files modified.")

if __name__ == "__main__":
    main()
