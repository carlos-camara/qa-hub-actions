import os
import xml.etree.ElementTree as ET
import glob
import sys

def parse_junit_xml(directory):
    total_tests = 0
    total_failures = 0
    total_errors = 0
    total_skipped = 0
    total_time = 0.0
    
    test_cases = []
    
    xml_files = glob.glob(os.path.join(directory, "**/*.xml"), recursive=True)
    if not xml_files:
        print(f"No XML files found in {directory}")
        return None

    for xml_file in xml_files:
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # JUnit can have <testsuites> or <testsuite> at the root
            suites = root.findall('.//testsuite') if root.tag != 'testsuite' else [root]
            
            for suite in suites:
                total_tests += int(suite.get('tests', 0))
                total_failures += int(suite.get('failures', 0))
                total_errors += int(suite.get('errors', 0))
                total_skipped += int(suite.get('skipped', 0))
                total_time += float(suite.get('time', 0))
                
                for case in suite.findall('testcase'):
                    name = case.get('name')
                    classname = case.get('classname', 'Default')
                    time = float(case.get('time', 0))
                    status = '✅'
                    
                    failure = case.find('failure')
                    error = case.find('error')
                    skipped = case.find('skipped')
                    
                    if failure is not None:
                        status = '❌'
                    elif error is not None:
                        status = '🔥'
                    elif skipped is not None:
                        status = '⏭️'
                        
                    if status != '✅':
                        test_cases.append({
                            'name': name,
                            'class': classname,
                            'status': status,
                            'time': time
                        })
        except Exception as e:
            print(f"Error parsing {xml_file}: {e}")

    passed = total_tests - total_failures - total_errors - total_skipped
    
    return {
        'total': total_tests,
        'passed': passed,
        'failed': total_failures + total_errors,
        'skipped': total_skipped,
        'time': total_time,
        'issues': test_cases
    }

def generate_markdown(results):
    if not results:
        return "### 🚦 No test results found."

    summary = ""
    summary += f"| Status | Count | Percentage |\n"
    summary += f"| :--- | :---: | :--- |\n"
    
    pass_pct = (results['passed'] / results['total'] * 100) if results['total'] > 0 else 0
    fail_pct = (results['failed'] / results['total'] * 100) if results['total'] > 0 else 0
    skip_pct = (results['skipped'] / results['total'] * 100) if results['total'] > 0 else 0
    
    summary += f"| ✅ Passed | {results['passed']} | {pass_pct:.1f}% |\n"
    summary += f"| ❌ Failed | {results['failed']} | {fail_pct:.1f}% |\n"
    summary += f"| ⏭️ Skipped | {results['skipped']} | {skip_pct:.1f}% |\n"
    summary += f"| **Total** | **{results['total']}** | **Duration: {results['time']:.2f}s** |\n\n"

    if results['issues']:
        summary += "#### 🔎 Failed/Skipped Details\n\n"
        summary += "| Test Case | Status | Time |\n"
        summary += "| :--- | :---: | :--- |\n"
        for issue in results['issues'][:15]: # Cap at 15 for PR readability
            summary += f"| `{issue['class']}`: {issue['name']} | {issue['status']} | {issue['time']:.2f}s |\n"
        
        if len(results['issues']) > 15:
            summary += f"\n*... and {len(results['issues']) - 15} more issues. See job artifacts for full reports.*"

    return summary

if __name__ == "__main__":
    reports_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    res = parse_junit_xml(reports_dir)
    md = generate_markdown(res)
    
    with open('test_summary.md', 'w', encoding='utf-8') as f:
        f.write(md)
    
    # Write outcome for action to read
    outcome = "FAILURE" if (res['failed'] > 0 or res['total'] == 0) else "SUCCESS"
    with open('test_outcome.txt', 'w', encoding='utf-8') as f:
        f.write(outcome)
        
    print(f"Markdown summary generated in test_summary.md (Outcome: {outcome})")
