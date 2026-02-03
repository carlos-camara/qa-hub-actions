# 📥 Upload Results to Repo

!!! info "At a Glance"
    - **Category**: Maintenance & CI
    - **Complexity**: Medium
    - **Version**: v1.0.0 (Stable)
    - **Primary Tool**: Git / GitHub Artifacts

Downloads standard QA Hub test reports and commits them back to the repository (e.g., for Wiki updates).

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `run-id` | GitHub Workflow Run ID to download artifacts from. | `REQUIRED` |
| `branch` | Target branch to push reports to. | `REQUIRED` |
| `upload-reports` | Process consolidated test reports? | `'true'` |
| `upload-perf` | Process Performance reports? | `'true'` |
| `commit-message` | Custom commit message. | `'docs: auto-generate integrated test reports and screenshots [skip ci]'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/upload-results@main
  with:
    run-id: ${{ github.run_id }}
    branch: "gh-pages"
```

---
*Automated reporting, directly in your source.*
