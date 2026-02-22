import os, re, shutil

# Ensure directories exist
os.makedirs('docs/actions', exist_ok=True)

# 1. Sync Root Files
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()
    
# Rewrite relative links from ./action-name to actions/action-name.md
readme_content = re.sub(r'\]\(\./([^/)]+)/?\)', r'](actions/\1.md)', readme_content)

with open('docs/index.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)
if os.path.exists('CONTRIBUTING.md'):
    shutil.copy2('CONTRIBUTING.md', 'docs/contributing.md')

# 2. Sync Action Files
exclude = ['.github', 'docs', 'site', 'venv_docs', '.git']
for d in os.listdir('.'):
    if os.path.isdir(d) and d not in exclude:
        readme_path = os.path.join(d, 'README.md')
        if os.path.exists(readme_path):
            shutil.copy2(readme_path, f'docs/actions/{d}.md')

# 3. Generate Navigation
nav = [
    "nav:",
    "  - Home: index.md",
    "  - Getting Started: installation.md",
    "  - Action Directory:"
]

for f in sorted(os.listdir('docs/actions')):
    if f.endswith('.md'):
        with open(f'docs/actions/{f}', 'r', encoding='utf-8') as file:
            first_line = file.readline()
            title = re.sub(r'<[^>]*>', '', first_line).replace('#', '').strip()
            nav.append(f"    - '{title}': actions/{f}")

nav.append("  - Contributing: contributing.md")

# 4. Update mkdocs.yml
with open('mkdocs.yml', 'r', encoding='utf-8') as f:
    c = f.read()

new_c = re.sub(r'nav:\s*-.*', '\n'.join(nav), c, flags=re.DOTALL)

with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    f.write(new_c)

print('Wiki synchronization complete!')
