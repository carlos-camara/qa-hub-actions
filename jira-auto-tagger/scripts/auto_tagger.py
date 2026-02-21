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
JIRA_PARENT_PLAN = os.environ.get("JIRA_PARENT_PLAN")

if not all([JIRA_URL, JIRA_USER, JIRA_API_TOKEN]):
    print("⚠️ Missing Jira credentials. Skipping auto-tagging.")
    sys.exit(0)

# Authentication
auth = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def link_to_parent_plan(issue_key, parent_plan_key):
    """Fallback: Links the task to the parent test plan issue via Issue Links if parent field is rejected."""
    print(f"  🔗 Fallback: Linking '{issue_key}' to parent plan '{parent_plan_key}' via IssueLink (Relates)...")
    url = f"{JIRA_URL}/rest/api/3/issueLink"
    
    payload = json.dumps({
        "type": {
            "name": "Relates"
        },
        "inwardIssue": {
            "key": parent_plan_key
        },
        "outwardIssue": {
            "key": issue_key
        }
    })
    
    try:
        response = requests.post(url, data=payload, headers=headers, auth=auth)
        if response.status_code == 201:
            print(f"  ✅ Successfully linked to {parent_plan_key} via IssueLink")
        else:
            print(f"  ⚠️ Failed issue link to {parent_plan_key}. Status: {response.status_code}")
    except Exception as e:
        print(f"  ⚠️ Error linking to parent plan: {e}")

def _build_jira_description(tags, steps):
    """Helper to build Atlassian Document Format description."""
    description_content = [
        {
            "type": "paragraph",
            "content": [{"type": "text", "text": "🚀 Automated test scenario generated from GitHub Actions.\n\n"}]
        }
    ]
    if tags:
        description_content.append({
            "type": "paragraph",
            "content": [{"type": "text", "text": "🏷️ Original Tags:", "marks": [{"type": "strong"}]}]
        })
        description_content.append({
            "type": "codeBlock",
            "attrs": {"language": "gherkin"},
            "content": [{"type": "text", "text": " ".join(tags)}]
        })
    if steps:
        description_content.append({
            "type": "paragraph",
            "content": [{"type": "text", "text": "📝 Scenario Steps:", "marks": [{"type": "strong"}]}]
        })
        description_content.append({
            "type": "codeBlock",
            "attrs": {"language": "gherkin"},
            "content": [{"type": "text", "text": "\n".join(steps)}]
        })
    return description_content

def check_jira_task_exists(issue_key):
    """Checks if a task exists in Jira."""
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}?fields=summary"
    try:
        response = requests.get(url, headers=headers, auth=auth)
        return response.status_code == 200
    except Exception:
        return False

def update_jira_task(issue_key, summary, tags, steps):
    """Updates an existing Jira Task, preserving execution history if present."""
    print(f"  ➜ Updating existing Jira Task: '{issue_key}'")
    
    # 1. Fetch existing description to preserve history
    existing_description = None
    get_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}?fields=description"
    try:
        resp = requests.get(get_url, headers=headers, auth=auth)
        if resp.status_code == 200:
            existing_description = resp.json().get('fields', {}).get('description')
    except Exception as e:
        print(f"  ⚠️ Could not fetch existing description for {issue_key}: {e}")

    # Extract history blocks
    history_blocks = []
    if existing_description and isinstance(existing_description, dict) and "content" in existing_description:
        content = existing_description["content"]
        history_header_idx = -1
        history_list_idx = -1
        
        for i, block in enumerate(content):
            if block.get("type") == "heading" and block.get("attrs", {}).get("level") == 2:
                for text_node in block.get("content", []):
                    if text_node.get("type") == "text" and "Historial de Ejecuciones" in text_node.get("text", ""):
                        history_header_idx = i
                        break
            if history_header_idx != -1 and i > history_header_idx:
                if block.get("type") == "bulletList":
                    history_list_idx = i
                    break
                elif block.get("type") == "heading":
                    break
                    
        if history_header_idx != -1:
            history_blocks.append(content[history_header_idx])
            if history_list_idx != -1:
                history_blocks.append(content[history_list_idx])

    # Build new description
    new_doc_content = _build_jira_description(tags, steps)
    
    # Append preserved history blocks if any
    if history_blocks:
        new_doc_content.extend(history_blocks)
        
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}"
    
    payload_dict = {
        "fields": {
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": new_doc_content
            }
        }
    }
    
    # Try setting parent directly
    if JIRA_PARENT_PLAN:
        payload_dict["fields"]["parent"] = {"key": JIRA_PARENT_PLAN}
        
    try:
        response = requests.put(url, json=payload_dict, headers=headers, auth=auth)
        if response.status_code == 204:
            print(f"  ✅ Updated Jira Task: {issue_key}")
            return True
        elif response.status_code == 400 and JIRA_PARENT_PLAN:
            print(f"  ⚠️ Jira rejected native parent Epic link for {issue_key}. Retrying without parent field...")
            # Retry without parent
            del payload_dict["fields"]["parent"]
            retry_res = requests.put(url, json=payload_dict, headers=headers, auth=auth)
            if retry_res.status_code == 204:
                print(f"  ✅ Updated Jira Task: {issue_key}")
                link_to_parent_plan(issue_key, JIRA_PARENT_PLAN)
                return True
            else:
                print(f"  ⚠️ Failed to update Jira task {issue_key}. Status: {retry_res.status_code}, Response: {retry_res.text}")
                return False
        else:
            print(f"  ⚠️ Failed to update Jira task {issue_key}. Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        print(f"  ⚠️ Error updating Jira task {issue_key}: {e}")
        return False

def create_jira_task(summary, tags, steps):
    """Creates a new Task in Jira and returns its Key."""
    print(f"  ➜ Creating Jira Task for: '{summary}'")
    url = f"{JIRA_URL}/rest/api/3/issue"
    
    payload_dict = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": _build_jira_description(tags, steps)
            },
            "issuetype": {"name": "Tarea"}
        }
    }
    
    if JIRA_PARENT_PLAN:
        payload_dict["fields"]["parent"] = {"key": JIRA_PARENT_PLAN}
        
    try:
        response = requests.post(url, json=payload_dict, headers=headers, auth=auth)
        if response.status_code == 201:
            issue_key = response.json()["key"]
            print(f"  ✅ Created Jira Task: {issue_key}")
            return issue_key
        elif response.status_code == 400 and JIRA_PARENT_PLAN:
            print(f"  ⚠️ Jira rejected native parent Epic link during creation. Retrying without parent field...")
            # Retry without parent
            del payload_dict["fields"]["parent"]
            retry_res = requests.post(url, json=payload_dict, headers=headers, auth=auth)
            if retry_res.status_code == 201:
                issue_key = retry_res.json()["key"]
                print(f"  ✅ Created Jira Task: {issue_key}")
                # Fallback to IssueLink
                link_to_parent_plan(issue_key, JIRA_PARENT_PLAN)
                return issue_key
            else:
                print(f"  ❌ Failed to create Jira task. Status: {retry_res.status_code}, Response: {retry_res.text}")
                return None
        else:
            print(f"  ❌ Failed to create Jira task. Status: {response.status_code}, Response: {response.text}")
            return None
    except Exception as e:
        print(f"  ❌ Error communicating with Jira: {e}")
        return None

def process_feature_file(file_path):
    """Reads a feature file, checks scenarios, creates or updates Jira tasks, and updates the file."""
    print(f"\n📄 Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    updated_lines = []
    file_modified = False
    
    i = 0
    current_feature_name = "Feature"
    while i < len(lines):
        line = lines[i]
        stripped_line = line.strip()
        
        if stripped_line.startswith('Feature:'):
             current_feature_name = stripped_line.split(':', 1)[1].strip()
        
        if stripped_line.startswith('Scenario:') or stripped_line.startswith('Scenario Outline:'):
            existing_jira_key = None
            existing_jira_key_index = -1
            first_tag_index = -1
            collected_tags = []
            
            # Look backwards for contiguous tags
            j = len(updated_lines) - 1
            while j >= 0:
                prev_line = updated_lines[j].strip()
                if not prev_line or prev_line.startswith('#'):
                    j -= 1
                    continue
                elif prev_line.startswith('@'):
                    first_tag_index = j
                    # Look for @PROJECT_KEY-123
                    match = re.search(fr'@{PROJECT_KEY}-(\d+)', prev_line)
                    if match:
                        existing_jira_key = f"{PROJECT_KEY}-{match.group(1)}"
                        existing_jira_key_index = j
                    
                    tags_in_line = [t.strip() for t in prev_line.split() if t.startswith('@')]
                    collected_tags = tags_in_line + collected_tags
                    j -= 1
                else:
                    break
            
            parts = stripped_line.split(':', 1)
            if len(parts) > 1:
                scenario_name = parts[1].strip()
                summary = f"{current_feature_name} - {scenario_name}"
                
                # Collect scenario steps
                collected_steps = []
                k = i + 1
                while k < len(lines):
                    next_line = lines[k].rstrip()
                    next_line_stripped = next_line.strip()
                    
                    if next_line_stripped.startswith('Scenario:') or \
                       next_line_stripped.startswith('Scenario Outline:') or \
                       next_line_stripped.startswith('@') or \
                       next_line_stripped.startswith('Feature:'):
                        break
                        
                    if next_line_stripped and not next_line_stripped.startswith('#'):
                         collected_steps.append(next_line.lstrip('\n\r'))
                    k += 1

                # Clean Jira tag from collected tags for the description payload to avoid redundancy
                tags_for_jira = [t for t in collected_tags if not t.startswith(f"@{PROJECT_KEY}-")]

                if existing_jira_key:
                    # Check if it actually exists in Jira
                    exists_in_jira = check_jira_task_exists(existing_jira_key)
                    if exists_in_jira:
                        update_jira_task(existing_jira_key, summary, tags_for_jira, collected_steps)
                    else:
                        print(f"  ⚠️ Tag @{existing_jira_key} found in code but deleted in Jira. Recreating...")
                        new_key = create_jira_task(summary, tags_for_jira, collected_steps)
                        if new_key:
                            # Replace the broken tag with the new one in the file
                            existing_tag_line = updated_lines[existing_jira_key_index]
                            updated_lines[existing_jira_key_index] = re.sub(fr'@{existing_jira_key}', f'@{new_key}', existing_tag_line)
                            file_modified = True
                else:
                    # Creating a brand new task
                    new_key = create_jira_task(summary, tags_for_jira, collected_steps)
                    if new_key:
                        if first_tag_index != -1:
                            existing_tag_line = updated_lines[first_tag_index]
                            indent = existing_tag_line[:len(existing_tag_line) - len(existing_tag_line.lstrip())]
                            content = existing_tag_line.lstrip()
                            updated_lines[first_tag_index] = f"{indent}@{new_key} {content}"
                        else:
                            indent = line[:len(line) - len(line.lstrip())]
                            updated_lines.append(f"{indent}@{new_key}\n")
                        file_modified = True
                        
        updated_lines.append(line)
        i += 1
        
    if file_modified:
        print(f"  💾 Updating file: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
    else:
        print("  ✓ Checked scenarios. No file updates necessary.")

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
