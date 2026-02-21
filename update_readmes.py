import os
import re

directories = [
    "collect-and-publish",
    "deploy-gh-pages",
    "deploy-reports-s3",
    "environment-health-check",
    "lint-codebase",
    "performance-baseline-check",
    "pr-labeler",
    "pr-milestoner",
    "pr-summarizer",
    "publish-test-results",
    "qa-release-notes",
    "security-audit",
    "setup-environment",
    "setup-services",
    "slack-notify",
    "sync-from-s3",
    "upload-results",
    "visual-regression-manager"
]

for d in directories:
    readme_path = os.path.join(d, "README.md")
    if not os.path.exists(readme_path):
        continue
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if already aligned
    if '<div align="center">' in content[:200]:
        print(f"Skipping {readme_path}, already formatted.")
        continue
        
    # Extract Title and Description 
    # Usually it's:
    # # 🧶 Action: Lint Codebase
    # 
    # Enforce consistent code quality standards...
    
    match = re.match(r"^#\s+(.+?)\n+(.+?)\n", content, re.MULTILINE)
    if match:
        original_title = match.group(1).strip()
        original_desc = match.group(2).strip()
        
        premium_header = f"""# <div align="center">{original_title}</div>

<div align="center">
  <p><i>{original_desc}</i></p>
</div>
"""
        # Replace the first two non-empty blocks
        new_content = re.sub(r"^#\s+(.+?)\n+(.+?)\n", premium_header + "\n", content, count=1, flags=re.MULTILINE)
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {readme_path}")
    else:
        print(f"Could not parse {readme_path}")

