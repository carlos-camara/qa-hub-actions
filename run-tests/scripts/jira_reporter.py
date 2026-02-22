import os
import json
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import sys
import re

# --- Configuration ---
JIRA_URL = os.environ.get("JIRA_URL")
JIRA_USER = os.environ.get("JIRA_USER")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")
PROJECT_KEY = os.environ.get("JIRA_PROJECT_KEY", "DAS")
REPORTS_DIR = os.environ.get("REPORTS_DIR", "reports")
MAX_HISTORY_ROWS = 10
JIRA_TEST_STATUS_FIELD_NAME = os.environ.get("JIRA_TEST_STATUS_FIELD")

if not all([JIRA_URL, JIRA_USER, JIRA_API_TOKEN]):
    print("⚠️ Missing Jira credentials. Skipping test reporting.")
    sys.exit(0)

auth = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get_custom_field_id(field_name):
    """Fetches the Jira field ID by its human-readable name."""
    if not field_name:
        return None
        
    print(f"  ➜ Looking up ID for custom field: '{field_name}'")
    url = f"{JIRA_URL}/rest/api/3/field"
    try:
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            for field in response.json():
                if field.get("name") == field_name:
                    return field["id"]
        else:
             print(f"  ⚠️ Failed to get fields. Response: {response.text}")
    except Exception as e:
        print(f"  ⚠️ Error finding custom field '{field_name}': {e}")
    return None

def update_issue_description(issue_key, status, error_log=None, system_out=None):
    """Fetches the Jira issue, updates its description to include a history table and the latest execution logs."""
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}"
    
    print(f"  ➜ Attempting to update Execution History Table in description for {issue_key}")
    try:
        # Fetch current issue to get the description
        resp_get = requests.get(url, headers=headers, auth=auth)
        if resp_get.status_code != 200:
            print(f"  ❌ Failed to fetch issue {issue_key} for description update. Status: {resp_get.status_code}")
            return False, None
            
        issue_data = resp_get.json()
        description = issue_data.get("fields", {}).get("description")
        parent_key = issue_data.get("fields", {}).get("parent", {}).get("key")
        
        # We need to manipulate the Atlassian Document Format (ADF) description
        if not description or not isinstance(description, dict) or "content" not in description:
            # Initialize empty ADF if it doesn't exist
            description = {
                "type": "doc",
                "version": 1,
                "content": []
            }
            
        content = description.get("content", [])
        
        from datetime import datetime
        import traceback
        run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status_emoji = "✅ PASSED" if status == "PASSED" else "❌ FAILED"
        
        # We'll use a simplified text approach for the history rather than building complex ADF tables
        # because ADF tables are extremely verbose and hard to manipulate safely here without a library.
        # Instead, we will append a "panel" or a "codeBlock" containing a simple ASCII table, 
        # or just a list of the last executions.
        
        # 1. Update the "📝 Scenario Steps" block with system_out logs if provided
        if system_out:
            steps_header_idx = -1
            for i, block in enumerate(content):
                 if block.get("type") == "paragraph":
                     for text_node in block.get("content", []):
                         if text_node.get("type") == "text" and "📝 Scenario Steps" in text_node.get("text", ""):
                             steps_header_idx = i
                             break
            
            if steps_header_idx != -1 and steps_header_idx + 1 < len(content):
                # The next block should be the codeBlock with the steps
                next_block = content[steps_header_idx + 1]
                if next_block.get("type") == "codeBlock":
                    next_block["content"] = [{"type": "text", "text": system_out}]
            else:
                 # If it doesn't exist, append it
                 content.append({
                     "type": "paragraph",
                     "content": [{"type": "text", "text": "📝 Scenario Steps:", "marks": [{"type": "strong"}]}]
                 })
                 content.append({
                     "type": "codeBlock",
                     "attrs": {"language": "gherkin"},
                     "content": [{"type": "text", "text": system_out}]
                 })

        # 2. Find if our History section already exists
        history_header_idx = -1
        history_list_idx = -1
        
        for i, block in enumerate(content):
            if block.get("type") == "heading" and block.get("attrs", {}).get("level") == 2:
                for text_node in block.get("content", []):
                    if text_node.get("type") == "text" and "Historial de Ejecuciones" in text_node.get("text", ""):
                        history_header_idx = i
                        break
            
            # Find the first bullet list *after* the header
            if history_header_idx != -1 and i > history_header_idx:
                 if block.get("type") == "bulletList":
                     history_list_idx = i
                     break
                 elif block.get("type") == "heading":
                     # Stop searching if we hit another section
                     break
                 
        # Create execution entry
        entry_text = f"[{run_date}] - Status: {status_emoji}"
        new_item = {
            "type": "listItem",
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": entry_text}]
                }
            ]
        }
        
        if history_header_idx == -1:
            # Add header and new list
            content.append({
                "type": "heading",
                "attrs": {"level": 2},
                "content": [{"type": "text", "text": "⏱️ Historial de Ejecuciones"}]
            })
            content.append({
                "type": "bulletList",
                "content": [new_item]
            })
        else:
            if history_list_idx != -1:
                # Append to existing list and keep only last MAX_HISTORY_ROWS
                list_items = content[history_list_idx].get("content", [])
                list_items.insert(0, new_item) # Insert at beginning
                if len(list_items) > MAX_HISTORY_ROWS:
                    list_items = list_items[:MAX_HISTORY_ROWS]
                content[history_list_idx]["content"] = list_items
            else:
                 # Header exists but no list right after, inject it
                 content.insert(history_header_idx + 1, {
                    "type": "bulletList",
                    "content": [new_item]
                 })
                 
        # Save back the description
        payload = json.dumps({
            "fields": {
                "description": description
            }
        })
        
        resp_put = requests.put(url, data=payload, headers=headers, auth=auth)
        if resp_put.status_code in [200, 204]:
            print(f"  ✅ Execution history updated in description for {issue_key}")
            return True, parent_key
        else:
            print(f"  ❌ Failed to update description for {issue_key}. Status: {resp_put.status_code}")
            return False, parent_key
            
    except Exception as e:
        print(f"  ❌ Error updating description history for {issue_key}: {e}")
        return False, None
        
def add_test_result(issue_key, test_name, status, error_log=None, custom_field_id=None, **kwargs):
    """Adds a comment or updates a custom field on the Jira issue with the test result."""
    print(f"  ➜ Reporting result for {issue_key}: {status}")
    
    # 1. Update Custom Field if configured
    if custom_field_id:
        url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}"
        # Jira Custom Field Dropdowns need the value inside an object {"value": "PASSED"}
        payload = json.dumps({
            "fields": {
                custom_field_id: {"value": status}
            }
        })
        try:
            response = requests.put(url, data=payload, headers=headers, auth=auth)
            if response.status_code in [200, 204]:
                print(f"  ✅ Custom field updated to {status} for {issue_key}")
            else:
                print(f"  ❌ Failed to update custom field. Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
             print(f"  ❌ Error updating custom field on {issue_key}: {e}")
             
    # 2. Transition Issue Status (if the user added PASSED/FAILED as actual workflow statuses)
    print(f"  ➜ Attempting to transition status for {issue_key} to '{status}'")
    url_transitions = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/transitions"
    try:
        # Get available transitions for this issue
        resp = requests.get(url_transitions, headers=headers, auth=auth)
        if resp.status_code == 200:
            transitions = resp.json().get("transitions", [])
            target_transition = None
            for t in transitions:
                t_name = t.get("name", "").upper()
                to_status_name = t.get("to", {}).get("name", "").upper()
                
                # Check if either the transition name itself or the target status name matches PASSED/FAILED
                if t_name == status or to_status_name == status:
                    target_transition = t
                    break
            
            if target_transition:
                transition_id = target_transition["id"]
                payload_trans = json.dumps({
                    "transition": {"id": transition_id}
                })
                post_resp = requests.post(url_transitions, data=payload_trans, headers=headers, auth=auth)
                if post_resp.status_code == 204:
                    print(f"  ✅ Status of {issue_key} successfully transitioned to '{status}' (via transition '{target_transition.get('name')}')")
                else:
                    print(f"  ❌ Failed to transition status. Response: {post_resp.text}")
            else:
                available_transitions = [f"{t.get('name')} -> {t.get('to', {}).get('name')}" for t in transitions]
                print(f"  ⚠️ No transition to '{status}' available for {issue_key}. Available: {available_transitions}")
        else:
            print(f"  ❌ Failed to get transitions for {issue_key}. Status: {resp.status_code}")
    except Exception as e:
        print(f"  ❌ Error transitioning issue {issue_key}: {e}")
             
    # 3. Update description with history table and execution steps logs
    _, parent_key = update_issue_description(issue_key, status, error_log, kwargs.get('system_out'))
    
    # 4. Add comment (only if it failed to provide the full stacktrace, preventing comment pollution on success)
    if status == "FAILED" and error_log:
        url_comment = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/comment"
        text_content = f"❌ Automated Test Execution: The test **FAILED**.\n\nError Log:\n{{code}}\n{error_log}\n{{code}}"
        
        payload_comment = json.dumps({
            "body": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{"type": "text", "text": text_content}]
                }]
            }
        })
        
        try:
            response = requests.post(url_comment, data=payload_comment, headers=headers, auth=auth)
            if response.status_code == 201:
                print(f"  ✅ Comment with error log added to {issue_key}")
            else:
                print(f"  ❌ Failed to add error comment. Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
            print(f"  ❌ Error communicating with Jira for comments: {e}")
            
    return parent_key

def get_jira_key_from_name(test_name):
     """Extracts the Jira key from the test name if it was injected by behaving tools or parses it if provided.
     In Behave XML reports from xUnit, the tags aren't always easily accessible, so we depend on either
     searching Jira or having the key injected into the scenario name. For this implementation, we will search Jira by summary."""
     
     # 1. Try to extract tag directly from the test name
     # Behave sometimes prefixes the scenario with tags like: "@CC-123 @tag2 Scenario Name"
     match = re.search(fr"@{PROJECT_KEY}-(\d+)", test_name)
     if match:
         return f"{PROJECT_KEY}-{match.group(1)}"
         
     # 2. Extract clean scenario name (remove tags if they are at the beginning but regex missed)
     clean_name = test_name
     if "@" in clean_name:
         # Behave JUnit reporter usually outputs "filename:line_number" in the classname,
         # but the name attribute might be just the scenario name.
         # Let's clean out any known tags just in case
         clean_name = re.sub(r'@[^\s]+\s+', '', clean_name).strip()
     
     # 3. Simple fallback: search Jira for an issue with this exact name
     url = f"{JIRA_URL}/rest/api/3/search"
     # Escape quotes in clean_name for JQL
     escaped_name = clean_name.replace('"', '\\"')
     jql = f'project = "{PROJECT_KEY}" AND issuetype = "Tarea" AND summary ~ "\\"{escaped_name}\\""'
     
     payload = json.dumps({"jql": jql, "maxResults": 1})
     
     try:
         response = requests.post(url, data=payload, headers=headers, auth=auth)
         if response.status_code == 200:
             data = response.json()
             if data.get("total", 0) > 0:
                 return data["issues"][0]["key"]
     except Exception as e:
         print(f"Error searching Jira: {e}")
         
     return None

def process_junit_xml(file_path, custom_field_id=None):
    """Parses a JUnit XML report and sends results to Jira."""
    print(f"\n📄 Parsing Report: {file_path}")
    affected_features = set()
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Determine if root is testsuite or testsuites
        testsuites = [root] if root.tag == "testsuite" else root.findall("testsuite")
        
        for testsuite in testsuites:
             for testcase in testsuite.findall("testcase"):
                 test_name = testcase.get("name")
                 if not test_name:
                     continue
                     
                 # Determine status
                 failure = testcase.find("failure")
                 error = testcase.find("error")
                 
                 status = "PASSED"
                 error_log = None
                 
                 if failure is not None:
                     status = "FAILED"
                     error_log = failure.text or failure.get("message", "Unknown failure")
                 elif error is not None:
                     status = "FAILED"
                     error_log = error.text or error.get("message", "Unknown error")
                     
                 # 1. First, try to extract Jira tag from <system-out> CDATA provided by Behave
                 jira_key = None
                 system_out_text = None
                 system_out = testcase.find("system-out")
                 if system_out is not None and system_out.text:
                     system_out_text = system_out.text.strip()
                     match = re.search(fr"@{PROJECT_KEY}-(\d+)", system_out_text)
                     if match:
                         jira_key = f"{PROJECT_KEY}-{match.group(1)}"
                 
                 # Feature name extraction from classname
                 # e.g., "dashboard.api.api_endpoints.System Endpoints Discovery" -> "System Endpoints Discovery"
                 classname = testcase.get("classname", "")
                 feature_name = classname.split('.')[-1] if '.' in classname else classname
                 
                 # We build the summary name to search if it wasn't injected
                 full_test_name = f"{feature_name} - {test_name}" if feature_name else test_name
                 
                 # 2. If not found in system-out, rely on the old logic (name parsing or Jira search)
                 if not jira_key:
                     jira_key = get_jira_key_from_name(full_test_name)
                 
                 if jira_key:
                     parent_key = add_test_result(jira_key, full_test_name, status, error_log, custom_field_id, system_out=system_out_text)
                     if parent_key:
                         affected_features.add(parent_key)
                 else:
                     print(f"  ⚠️ Could not find Jira ticket for scenario: '{test_name}'. Ensure auto_tagger ran first.")

    except Exception as e:
        print(f"❌ Error processing XML {file_path}: {e}")
        
    return affected_features

def find_xml_reports(directory):
    """Recursively finds all .xml files in a directory."""
    xml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".xml"):
                xml_files.append(os.path.join(root, file))
    return xml_files

def evaluate_feature_rollup(feature_key):
    """Evaluates the status of all subtasks of a feature and transitions the feature accordingly."""
    print(f"\n🔄 Evaluating status rollup for Feature Task {feature_key}...")
    jql = f'parent = "{feature_key}"'
    url = f"{JIRA_URL}/rest/api/3/search"
    payload = json.dumps({"jql": jql, "fields": ["status", JIRA_TEST_STATUS_FIELD_NAME] if JIRA_TEST_STATUS_FIELD_NAME else ["status"]})
    
    try:
        response = requests.post(url, data=payload, headers=headers, auth=auth)
        if response.status_code == 200:
            issues = response.json().get("issues", [])
            if not issues:
                print(f"  ⚠️ No subtasks found for {feature_key}.")
                return
            
            all_passed = True
            any_failed = False
            
            custom_field_id = get_custom_field_id(JIRA_TEST_STATUS_FIELD_NAME)

            for issue in issues:
                status_name = issue.get("fields", {}).get("status", {}).get("name", "").upper()
                status_category = issue.get("fields", {}).get("status", {}).get("statusCategory", {}).get("key", "")
                
                # Check custom field if available, fallback to task status name/category
                test_status = None
                if custom_field_id and issue.get("fields", {}).get(custom_field_id):
                    field_val = issue.get("fields", {}).get(custom_field_id)
                    test_status = field_val.get("value", "").upper() if isinstance(field_val, dict) else str(field_val).upper()
                else:
                    test_status = status_name
                
                # A subtask is a failure if explicitly failed
                if "FAIL" in test_status:
                    any_failed = True
                    all_passed = False
                # If it's not FAILED but also not explicitly PASSED (or its category isn't "done"), it's pending
                elif "PASS" not in test_status and status_category != "done":
                    all_passed = False 
                    
            target_status = None
            if any_failed:
                target_status = "FAILED"
            elif all_passed:
                target_status = "PASSED"
                
            if target_status:
                print(f"  ➜ Attempting to transition Feature {feature_key} to '{target_status}'")
                url_transitions = f"{JIRA_URL}/rest/api/3/issue/{feature_key}/transitions"
                resp = requests.get(url_transitions, headers=headers, auth=auth)
                if resp.status_code == 200:
                    transitions = resp.json().get("transitions", [])
                    target_transition = None
                    for t in transitions:
                        t_name = t.get("name", "").upper()
                        to_name = t.get("to", {}).get("name", "").upper()
                        if target_status in t_name or target_status in to_name:
                            target_transition = t
                            break
                            
                    # Fallback: if 'PASSED' transition doesn't exist but 'DONE' does
                    if not target_transition and target_status == "PASSED":
                        for t in transitions:
                            to_cat = t.get("to", {}).get("statusCategory", {}).get("key", "")
                            if to_cat == "done":
                                target_transition = t
                                break

                    if target_transition:
                        payload_trans = json.dumps({"transition": {"id": target_transition["id"]}})
                        post_resp = requests.post(url_transitions, data=payload_trans, headers=headers, auth=auth)
                        if post_resp.status_code == 204:
                            print(f"  ✅ Feature {feature_key} successfully transitioned to '{target_transition.get('to', {}).get('name')}'")
                        else:
                            print(f"  ❌ Failed to transition Feature. Response: {post_resp.text}")
                    else:
                         print(f"  ⚠️ No transition mapped to '{target_status}' available for Feature {feature_key}.")
                else:
                    print(f"  ❌ Failed to get transitions for Feature {feature_key}. Status: {resp.status_code}")
        else:
            print(f"  ❌ Failed to search subtasks for {feature_key}. Status: {response.status_code}")
    except Exception as e:
        print(f"  ❌ Error evaluating rollup for {feature_key}: {e}")

if __name__ == "__main__":
    print(f"🚀 Starting Jira Reporter. Looking for reports in '{REPORTS_DIR}'")
    
    if not os.path.exists(REPORTS_DIR):
        print(f"⚠️ Reports directory '{REPORTS_DIR}' does not exist.")
        sys.exit(0)
        
    xml_files = find_xml_reports(REPORTS_DIR)
    
    if not xml_files:
        print(f"⚠️ No XML report files found in '{REPORTS_DIR}'.")
    else:
        custom_field_id = get_custom_field_id(JIRA_TEST_STATUS_FIELD_NAME)
        if custom_field_id:
            print(f"  🔹 Using Custom Field: '{JIRA_TEST_STATUS_FIELD_NAME}' (ID: {custom_field_id})")
        else:
            if JIRA_TEST_STATUS_FIELD_NAME:
                print(f"  ⚠️ Custom Field '{JIRA_TEST_STATUS_FIELD_NAME}' not found. Falling back to comments.")
            else:
                print(f"  🔹 No Custom Field configured for test status updating. Using comments.")
                
        all_affected_features = set()
        for file in xml_files:
            features = process_junit_xml(file, custom_field_id)
            all_affected_features.update(features)
            
        if all_affected_features:
            for feature_key in all_affected_features:
                evaluate_feature_rollup(feature_key)
            
    print("\n🏁 Jira Reporting complete.")
