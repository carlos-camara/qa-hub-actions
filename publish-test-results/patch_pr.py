import sys
import re
import os

try:
    # Read PR body from environment variable
    body = os.environ.get('CURRENT_BODY', '')
    
    # Read test summary
    summary = ""
    if os.path.exists('test_summary.md'):
        with open('test_summary.md', 'r', encoding='utf-8') as f:
            summary = f.read()
    else:
        print("Warning: test_summary.md not found.", file=sys.stderr)
    
    # Read test outcome
    outcome = "FAILURE"
    if os.path.exists('test_outcome.txt'):
        with open('test_outcome.txt', 'r', encoding='utf-8') as f:
            outcome = f.read().strip()

    anchor = '## 🚦 Test Results'
    
    # Regex to find the anchor and potentially existing content until next header or end
    # We use a pattern that captures:
    # 1. The anchor itself
    # 2. Any content following it (non-greedy)
    # 3. The start of the next section (## ) or end of string ($)
    pattern = rf'({re.escape(anchor)})(.*?)(\n## |$)'
    
    if anchor in body:
        # Replace existing section using a callback to avoid backslash escaping issues
        def replacement(match):
            # match.group(3) contains the next header or EOF, so we preserve it
            return match.group(1) + '\n\n' + summary + match.group(3)
            
        body = re.sub(pattern, replacement, body, flags=re.DOTALL)
    else:
        # Append if not found
        # Ensure we have some spacing
        if body and not body.endswith('\n'):
            body += '\n'
        body = body + '\n' + anchor + '\n\n' + summary

    # Auto-check "Automated Tests" box if success
    if outcome == 'SUCCESS':
        # Use regex to be robust against whitespace or minor formatting differences
        # Matches: - [ ] 🧪 **Automated Tests**
        pattern_check = r'-\s*\[\s*\]\s*🧪\s*\*\*Automated Tests\*\*'
        replacement_check = '- [x] 🧪 **Automated Tests**'
        
        body = re.sub(pattern_check, replacement_check, body)
        
    # Output the new body to stdout
    print(body)

except Exception as e:
    print(f"Error patching PR: {e}", file=sys.stderr)
    sys.exit(1)
