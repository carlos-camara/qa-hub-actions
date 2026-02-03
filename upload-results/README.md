# 📥 Upload Test Results to Repo

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Downloads standard QA Hub test reports and commits them to the repository's specified branch.

## ⚡ Quick Info

- **Category**: Maintenance & CI
- **Complexity**: Medium
- **Version**: v1.0.0

## 🚀 Usage

```yaml
- uses: carlos-camara/qa-hub-actions/upload-results@main
  with:
    run-id: ${{ github.run_id }}
    branch: "gh-pages"
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `run-id` | GitHub Workflow Run ID. | `REQUIRED` |
| `branch` | Target branch name. | `REQUIRED` |
| `upload-reports` | Process test reports? | `'true'` |
| `commit-message` | Custom commit message. | `'docs: auto-generate...'` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/upload-results/)
