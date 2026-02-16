import os
import json
import summarize

# Mock environment variables
os.environ['GITHUB_EVENT_PATH'] = 'mock_event.json'
os.environ['GITHUB_TOKEN'] = 'mock_token'
os.environ['TARGET'] = 'file' # Custom target for testing to avoid gh calls

# Mock event data
event_data = {
    "pull_request": {
        "number": 123,
        "title": "Refactor Dashboard and Update Docs",
        "base": {"sha": "HEAD~1"}
    }
}

with open('mock_event.json', 'w', encoding='utf-8') as f:
    json.dump(event_data, f)

# Mock git command results in summarize.py by monkeypatching run_command
def mock_run_command(command):
    if "git diff --name-status" in command:
        return "M\tApp.tsx\nM\tREADME.md\nA\tfeatures/dashboard/gui/gui_test_runs.feature\nD\tcomponents/IncidentView.tsx"
    if "git diff -U0" in command:
        return "-def old_func\n+def new_func"
    return ""

summarize.run_command = mock_run_command

# Mock gh commands
def mock_gh_edit(pr, body_file):
    print(f"MOCK: Updating PR {pr} with {body_file}")

# Run main logic
try:
    summarize.main()
    print("\n--- GENERATED SUMMARY ---\n")
    if os.path.exists('final_pr_body.md'):
        with open('final_pr_body.md', 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print("Error: final_pr_body.md not generated")
except Exception as e:
    print(f"Execution failed: {e}")
finally:
    # Cleanup
    if os.path.exists('mock_event.json'): os.remove('mock_event.json')
