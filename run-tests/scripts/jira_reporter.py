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

if not all([JIRA_URL, JIRA_USER, JIRA_API_TOKEN]):
    print("⚠️ Missing Jira credentials. Skipping test reporting.")
    sys.exit(0)

auth = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def add_test_result(issue_key, test_name, status, error_log=None):
    """Adds a comment to the Jira issue with the test result."""
    print(f"  ➜ Reporting result for {issue_key}: {status}")
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/comment"
    
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
        response = requests.post(url, data=payload, headers=headers, auth=auth)
        if response.status_code == 201:
            print(f"  ✅ Result added to {issue_key}")
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

def process_junit_xml(file_path):
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
                     
                 # For our auto_tagger flow, we expect the Jira Task to already exist.
                 # Let's search for it.
                 jira_key = get_jira_key_from_name(test_name)
                 
                 if jira_key:
                     add_test_result(jira_key, test_name, status, error_log)
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
        for file in xml_files:
            process_junit_xml(file)
            
    print("\n🏁 Jira Reporting complete.")
