# 🚀 Python Auto-Release

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Automates versioning, changelogs, and GitHub Releases for Python projects using Python Semantic Release.

## ⚡ Quick Info

- **Category**: Maintenance & CI
- **Complexity**: Medium
- **Version**: v1.0.0

## 🚀 Usage

```yaml
- uses: carlos-camara/qa-hub-actions/python-auto-release@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `github-token` | Personal access token or GITHUB_TOKEN. | `REQUIRED` |
| `python-version` | Python version to use. | `'3.11'` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/python-auto-release/)
