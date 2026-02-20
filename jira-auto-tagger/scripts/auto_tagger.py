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
    """Links the newly created task to a parent test plan issue."""
    print(f"  🔗 Linking '{issue_key}' to parent plan '{parent_plan_key}'...")
    url = f"{JIRA_URL}/rest/api/3/issueLink"
    
    payload = json.dumps({
        "type": {
            "name": "Relates"  # Using standard 'Relates' link type
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
            print(f"  ✅ Successfully linked to {parent_plan_key}")
        else:
            print(f"  ⚠️ Failed to link to {parent_plan_key}. Status: {response.status_code}")
    except Exception as e:
        print(f"  ⚠️ Error linking to parent plan: {e}")

def create_jira_task(summary, tags, steps):
    """Creates a new Task in Jira and returns its Key."""
    print(f"  ➜ Creating Jira Task for: '{summary}'")
    url = f"{JIRA_URL}/rest/api/3/issue"
    
    # Format tags and steps for Jira description (Atlassian Document Format)
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
    
    payload = json.dumps({
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": description_content
            },
            "issuetype": {"name": "Tarea"}
        }
    })
    
    try:
        response = requests.post(url, data=payload, headers=headers, auth=auth)
        if response.status_code == 201:
            issue_key = response.json()["key"]
            print(f"  ✅ Created Jira Task: {issue_key}")
            
            # Link to parent plan if configured
            if JIRA_PARENT_PLAN:
                link_to_parent_plan(issue_key, JIRA_PARENT_PLAN)
                
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
            first_tag_index = -1
            collected_tags = []
            
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
                    first_tag_index = j  # Keep tracking the earliest tag line in this block
                    if f'@{PROJECT_KEY}-' in prev_line:
                        has_jira_tag = True
                        break
                    
                    # Collect existing tags for description
                    tags_in_line = [t.strip() for t in prev_line.split() if t.startswith('@')]
                    # Prepend since we are iterating backwards
                    collected_tags = tags_in_line + collected_tags
                    j -= 1
                else:
                    # We hit a non-tag, non-empty, non-comment line, stop searching backwards
                    break
            
            if not has_jira_tag:
                # Extract scenario name
                parts = stripped_line.split(':', 1)
                if len(parts) > 1:
                    scenario_name = parts[1].strip()
                    
                    # Collect scenario steps by looking ahead
                    collected_steps = []
                    k = i + 1
                    while k < len(lines):
                        next_line = lines[k].rstrip()
                        next_line_stripped = next_line.strip()
                        
                        # Stop if we hit the next Scenario, a new tag block, or Feature
                        if next_line_stripped.startswith('Scenario:') or \
                           next_line_stripped.startswith('Scenario Outline:') or \
                           next_line_stripped.startswith('@') or \
                           next_line_stripped.startswith('Feature:'):
                            break
                            
                        # If it's a step (Given, When, Then, And, But, *, or table row |)
                        if next_line_stripped and not next_line_stripped.startswith('#'):
                             # Keep original indentation relative to the scenario
                             collected_steps.append(next_line.lstrip('\n\r'))
                        k += 1
                        
                    # Create Jira Task with tags and steps
                    jira_key = create_jira_task(scenario_name, collected_tags, collected_steps)
                    
                    if jira_key:
                        if first_tag_index != -1:
                            # Prepend to the first existing tag line
                            existing_tag_line = updated_lines[first_tag_index]
                            indent = existing_tag_line[:len(existing_tag_line) - len(existing_tag_line.lstrip())]
                            content = existing_tag_line.lstrip()
                            updated_lines[first_tag_index] = f"{indent}@{jira_key} {content}"
                        else:
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
