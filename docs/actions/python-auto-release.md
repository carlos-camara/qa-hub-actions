# 🚀 Python Auto-Release

/// details | At a Glance
- **Category**: Maintenance & CI
- **Complexity**: Medium
- **Version**: v1.0.0 (Stable)
- **Primary Tool**: Python Semantic Release
///

Hands-free versioning, changelog generation, and GitHub Releases for Python packages.

## 📖 Overview

Standardizes the use of `python-semantic-release`. It analyzes your commit messages (following Conventional Commits), bumps the version, updates the changelog, and creates a GitHub Release with one action.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `github-token` | Token with permissions to create releases. | `REQUIRED` |
| `python-version` | Python version for the release process. | `'3.11'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/python-auto-release@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

---
*Professional version management, automated.*
