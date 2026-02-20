import os
import re
import requests
import json
from requests.auth import HTTPBasicAuth
import sys

# --- Configuration ---
JIRA_URL = os.environ.get("JIRA_URL")
JIRA_USER = os.environ.get("JIRA_USER")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")
PROJECT_KEY = os.environ.get("JIRA_PROJECT_KEY", "DAS")
FEATURES_DIR = os.environ.get("FEATURES_DIR", "features")

if not all([JIRA_URL, JIRA_USER, JIRA_API_TOKEN]):
    print("⚠️ Missing Jira credentials. Skipping auto-tagging.")
    sys.exit(0)

# Authentication
auth = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def create_jira_task(summary):
    """Creates a new Task in Jira and returns its Key."""
    print(f"  ➜ Creating Jira Task for: '{summary}'")
    url = f"{JIRA_URL}/rest/api/3/issue"
    
    payload = json.dumps({
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{"type": "text", "text": "Automated test scenario generated from GitHub Actions."}]
                }]
            },
            "issuetype": {"name": "Tarea"}
        }
    })
    
    try:
        response = requests.post(url, data=payload, headers=headers, auth=auth)
        if response.status_code == 201:
            issue_key = response.json()["key"]
            print(f"  ✅ Created Jira Task: {issue_key}")
            return issue_key
        else:
            print(f"  ❌ Failed to create Jira task. Status: {response.status_code}, Response: {response.text}")
            return None
    except Exception as e:
        print(f"  ❌ Error communicating with Jira: {e}")
        return None

def process_feature_file(file_path):
    """Reads a feature file, finds untagged scenarios, creates Jira tasks, and updates the file."""
    print(f"\n📄 Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    updated_lines = []
    file_modified = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped_line = line.strip()
        
        # Check if the line is a Scenario or Scenario Outline
        if stripped_line.startswith('Scenario:') or stripped_line.startswith('Scenario Outline:'):
            has_jira_tag = False
            
            # Look backwards through updated_lines for contiguous tags
            j = len(updated_lines) - 1
            while j >= 0:
                prev_line = updated_lines[j].strip()
                if not prev_line or prev_line.startswith('#'):
                    # Skip empty lines or comments
                    j -= 1
                    continue
                elif prev_line.startswith('@'):
                    # It's a tag line, check if it contains the Jira tag
                    if f'@{PROJECT_KEY}-' in prev_line:
                        has_jira_tag = True
                        break
                    j -= 1
                else:
                    # We hit a non-tag, non-empty, non-comment line, stop searching backwards
                    break
            
            if not has_jira_tag:
                # Extract scenario name
                parts = stripped_line.split(':', 1)
                if len(parts) > 1:
                    scenario_name = parts[1].strip()
                    
                    # Create Jira Task
                    jira_key = create_jira_task(scenario_name)
                    
                    if jira_key:
                        # Add the tag right before the Scenario line
                        indent = line[:len(line) - len(line.lstrip())]
                        updated_lines.append(f"{indent}@{jira_key}\n")
                        file_modified = True
        
        updated_lines.append(line)
        i += 1
        
    if file_modified:
        print(f"  💾 Updating file: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
    else:
        print("  ✓ No untagged scenarios found.")

def find_feature_files(directory):
    """Recursively finds all .feature files in a directory."""
    feature_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".feature"):
                feature_files.append(os.path.join(root, file))
    return feature_files

if __name__ == "__main__":
    print(f"🚀 Starting Jira Auto-Tagger for project '{PROJECT_KEY}' in directory '{FEATURES_DIR}'")
    feature_files = find_feature_files(FEATURES_DIR)
    
    if not feature_files:
        print(f"⚠️ No .feature files found in '{FEATURES_DIR}'.")
    else:
        for file in feature_files:
            process_feature_file(file)
            
    print("\n🏁 Auto-Tagging complete.")
