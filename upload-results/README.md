# 📥 Action: Upload Results

Consolidate and archive surgical test reports, visual evidence, and performance metadata directly into your repository branch for persistent history.

---

## 🚀 Key Impact

- **📥 Artifact Consolidation**: Automatically downloads and merges unified test reports and GUI screenshots from workflow runs.
- **💾 Repository Persistence**: Commits and pushes the consolidated results back to a specified branch (e.g., `gh-pages` or `results`).
- **📸 Screenshot Capture**: Handles visual evidence by organizing artifacts into a dedicated `screenshots` resource directory.
- **🤝 Standardized Layout**: Enforces the official QA Hub directory structure for reports and assets.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `run-id` | **Yes** | - | GitHub Run ID to pull consolidated artifacts from. |
| `branch` | **Yes** | - | Target branch for committing the results. |
| `upload-reports` | No | `true` | Toggle for processing test results and screenshots. |
| `upload-perf` | No | `true` | Toggle for processing performance metadata. |
| `commit-message` | No | (Table) | Custom Git commit message for the updates. |

---

## ⚡ Quick Start

```yaml
- name: 📥 Upload persistent results
  uses: carlos-camara/qa-hub-actions/upload-results@main
  with:
    run-id: ${{ github.run_id }}
    branch: "gh-pages"
    commit-message: "chore: update test dashboard artifacts"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/upload-results/)
</div>
