# 📤 Upload Test Results to Repo

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**Automatically commit and push test reports back to the repository.**

</div>

---

## 🚀 Overview

This action closes the loop on reporting by checking test artifacts back into the repository. Only use this if you want to store reports (like HTML dossiers or history files) directly in your git history (e.g., on a `gh-pages` branch or a dedicated `results` branch).

### Key Features
- **🤖 Auto-Commit**: Detects changes in reports and screenshots and commits them.
- **🔀 Branch Targeting**: Can push to a specific branch (e.g., `gh-pages`).
- **♻️ Smart Merge**: Merges new results with existing ones in the target folder.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/upload-results@v1
  with:
    run-id: ${{ github.run_id }}
    branch: 'gh-pages'
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `run-id` | **REQUIRED**. Run ID to download artifacts from. | **Yes** | - |
| `branch` | **REQUIRED**. Target branch to push to. | **Yes** | - |
| `upload-reports` | Process consolidated test reports? | No | `true` |
| `upload-perf` | Process Performance reports? | No | `true` |
| `commit-message` | Custom commit message. | No | `docs: ...` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
