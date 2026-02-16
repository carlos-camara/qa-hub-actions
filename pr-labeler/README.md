# 🏷️ PR Labeler

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Automatically labels pull requests based on the paths of files that are changed.

## ⚡ Quick Info

- **Category**: Maintenance & CI
- **Complexity**: Low
- **Version**: v5.0.0

## 🚀 Usage

```yaml
- name: Label PR
  uses: carlos-camara/qa-hub-actions/pr-labeler@main
  with:
    repo-token: ${{ secrets.GITHUB_TOKEN }}
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `repo-token` | GITHUB_TOKEN for the repo. | `${{ github.token }}` |
| `configuration-path` | Path to labeler config. | `.github/labeler.yml` |
| `sync-labels` | Remove labels on revert? | `'true'` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/pr-labeler/)
