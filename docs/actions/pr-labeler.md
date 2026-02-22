# 🏷️ Action: PR Labeler

<div align="center">
  <p><i>Automatically categorize Pull Requests based on modified file paths to maintain repository hygiene and streamline code reviews.</i></p>
</div>

---

> [!IMPORTANT]
> The **PR Labeler** surgically applies labels (e.g., `Frontend`, `Backend`, `DevOps`) to Pull Requests by evaluating path-matching rules defined in your repository. This ensures zero-overhead triage and absolute organizational consistency.

## 🚀 Quick Start

Drop this snippet into your PR intelligence workflow:

```yaml
steps:
  - name: 🏷️ Triage PR
    uses: carlos-camara/qa-hub-actions/pr-labeler@main
    with:
      repo-token: ${{ secrets.GITHUB_TOKEN }}
      configuration-path: ".github/labeler.yml"
```

## ⚙️ Configuration

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `repo-token` | GitHub Token for applying labels. | No | `${{ github.token }}` |
| `configuration-path` | Path to the YAML file defining labeling rules. | No | `.github/labeler.yml` |
| `sync-labels` | Remove labels when files no longer match rules. | No | `true` |

---



---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-labeler/)
</div>
