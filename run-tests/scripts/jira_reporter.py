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

def add_test_result(issue_key, test_name, status, error_log=None, custom_field_id=None):
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
             
    # 3. Add comment
    # If using custom fields, we only add a comment if there is an error log to attach
    if custom_field_id and not error_log:
         return # Skip comment if it passed and we already updated the field
         
    url_comment = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/comment"
    
    if status == "PASSED":
        text_content = f"✅ Automated Test Execution: The test **PASSED**."
    else:
        text_content = f"❌ Automated Test Execution: The test **FAILED**."
        if error_log:
             text_content += f"\n\nError Log:\n{{code}}\n{error_log}\n{{code}}"
             
    payload = json.dumps({
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
        response = requests.post(url_comment, data=payload, headers=headers, auth=auth)
        if response.status_code == 201:
            print(f"  ✅ Comment added to {issue_key}")
        else:
            print(f"  ❌ Failed to add comment. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"  ❌ Error communicating with Jira: {e}")

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
                 system_out = testcase.find("system-out")
                 if system_out is not None and system_out.text:
                     match = re.search(fr"@{PROJECT_KEY}-(\d+)", system_out.text)
                     if match:
                         jira_key = f"{PROJECT_KEY}-{match.group(1)}"
                 
                 # 2. If not found in system-out, rely on the old logic (name parsing or Jira search)
                 if not jira_key:
                     jira_key = get_jira_key_from_name(test_name)
                 
                 if jira_key:
                     add_test_result(jira_key, test_name, status, error_log, custom_field_id)
                 else:
                     print(f"  ⚠️ Could not find Jira ticket for scenario: '{test_name}'. Ensure auto_tagger ran first.")

    except Exception as e:
        print(f"❌ Error processing XML {file_path}: {e}")

def find_xml_reports(directory):
    """Recursively finds all .xml files in a directory."""
    xml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".xml"):
                xml_files.append(os.path.join(root, file))
    return xml_files

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
                
        for file in xml_files:
            process_junit_xml(file, custom_field_id)
            
    print("\n🏁 Jira Reporting complete.")
