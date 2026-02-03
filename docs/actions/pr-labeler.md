# 🏷️ PR Labeler

Automatic categorization of Pull Requests based on the modified file paths.

## 📖 Overview

Keeps your repository organized by automatically applying labels (e.g., `Core`, `Documentation`, `Tests`) based on a configuration file.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `repo-token` | The `GITHUB_TOKEN`. | `${{ github.token }}` |
| `configuration-path` | Path to the labeler rules. | `'.github/labeler.yml'` |
| `sync-labels` | Remove labels if files are removed. | `'true'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/pr-labeler@main
  with:
    sync-labels: 'true'
```

---
*Stay organized, even at scale.*
