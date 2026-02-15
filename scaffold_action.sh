#!/bin/bash
# 🚀 QA Hub Action Scaffolder
# Usage: ./scaffold_action.sh <action-name>

ACTION_NAME=$1

if [ -z "$ACTION_NAME" ]; then
  echo "Usage: ./scaffold_action.sh <action-name>"
  exit 1
fi

mkdir -p "$ACTION_NAME"

# Create action.yml
cat <<EOF > "$ACTION_NAME/action.yml"
name: '$(echo $ACTION_NAME | sed -e "s/-/ /g" -e "s/\b\(.\)/\u\1/g")'
description: '🚀 Description of what this action does.'
branding:
  icon: 'package'
  color: 'blue'
inputs:
  my-input:
    description: 'Example input'
    required: true

runs:
  using: 'composite'
  steps:
    - name: Run Action
      shell: bash
      run: echo "Hello from $ACTION_NAME"
EOF

# Create README.md (Gold Standard)
cat <<EOF > "$ACTION_NAME/README.md"
# 🚀 Action: $(echo $ACTION_NAME | sed -e "s/-/ /g" -e "s/\b\(.\)/\u\1/g")

> Short value proposition.

## 📖 What it does
- **Feature 1**: Description.
- **Feature 2**: Description.

## 🛠️ Configuration
| Input | Description | Default |
| :--- | :--- | :--- |
| \`my-input\` | Example input. | \`REQUIRED\` |

## 🚀 Usage

\`\`\`yaml
- uses: carlos-camara/qa-hub-actions/$ACTION_NAME@main
  with:
    my-input: "value"
\`\`\`
EOF

echo "✅ Created action: $ACTION_NAME"
