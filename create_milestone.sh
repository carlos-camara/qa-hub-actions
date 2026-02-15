#!/bin/bash
# 🎯 QA Hub Milestone Creator
# Usage: ./create_milestone.sh "Title" [Due Date YYYY-MM-DD] [Description]

TITLE=$1
DUE_DATE=$2
DESCRIPTION=${3:-"Milestone created via automation"}

if [ -z "$TITLE" ]; then
  echo "Usage: ./create_milestone.sh \"<Title>\" [YYYY-MM-DD] [\"Description\"]"
  echo "Example: ./create_milestone.sh \"v2.0.0\" 2024-12-31 \"Major Release\""
  exit 1
fi

# Build arguments
ARGS=(-f title="$TITLE" -f state="open" -f description="$DESCRIPTION")

if [ ! -z "$DUE_DATE" ]; then
  # Validate date format roughly
  if [[ "$DUE_DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    ARGS+=(-f due_on="${DUE_DATE}T00:00:00Z")
  else
    echo "⚠️ Warning: Date format must be YYYY-MM-DD. Ignoring date."
  fi
fi

echo "🚀 Creating milestone: $TITLE..."
gh api repos/:owner/:repo/milestones "${ARGS[@]}"

if [ $? -eq 0 ]; then
  echo "✅ Milestone '$TITLE' created successfully!"
else
  echo "❌ Failed to create milestone."
fi
