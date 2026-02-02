# 🏷️ PR Auto-Labeler

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**Automatically categorize and label Pull Requests based on modified file paths.**

</div>

---

## 🚀 Overview

The PR Labeler helps maintain organization in busy repositories by automatically tagging Pull Requests. It analyzes the files changed in a PR and applies labels according to rules defined in a configuration file (usually `.github/labeler.yml`).

### Key Features
- **📂 Path-Based Labeling**: Apply labels like `Frontend`, `Backend`, or `Documentation` based on directory changes.
- **🔄 Label Sync**: Automatically removes labels if the corresponding files are removed from the PR.
- **⚡ Fast Execution**: Built on top of the industry-standard `actions/labeler`.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/pr-labeler@v1
  with:
    repo-token: ${{ secrets.GITHUB_TOKEN }}
    configuration-path: '.github/labeler.yml'
```

### Example `.github/labeler.yml`

```yaml
Frontend:
  - 'components/**/*'
  - 'styles/**/*'

Backend:
  - 'services/**/*'
  - 'api/**/*'

QA:
  - 'tests/**/*'
  - 'features/**/*'

Documentation:
  - '*.md'
  - 'docs/**/*'
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `repo-token` | GITHUB_TOKEN for label management. | No | `${{ github.token }}` |
| `configuration-path` | Path to the labeling rules file. | No | `.github/labeler.yml` |
| `sync-labels` | Remove labels when matching files are reverted. | No | `true` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
