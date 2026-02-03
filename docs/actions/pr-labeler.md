# 🏷️ PR Labeler

!!! info "At a Glance"
    - **Category**: Maintenance & CI
    - **Complexity**: Low
    - **Version**: v5.0.0 (Stable)
    - **Primary Tool**: actions/labeler

Automatically manage Pull Request labels based on modified file paths. Keeps your project organized without manual effort.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `repo-token` | The `GITHUB_TOKEN` for the repository. | `${{ github.token }}` |
| `configuration-path` | The path to the labeler configuration file. | `.github/labeler.yml` |
| `sync-labels` | Whether to remove labels when matching files are reverted. | `true` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/pr-labeler@main
  with:
    repo-token: ${{ secrets.GITHUB_TOKEN }}
    configuration-path: ".github/my-custom-labels.yml"
```

---
*Organization at scale.*
