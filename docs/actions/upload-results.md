# 📤 Upload Results to Repo

!!! info "At a Glance"
    - **Category**: Reporting
    - **Complexity**: Low
    - **Recent Version**: v1.0.0 (Stable)
    - **Primary Tool**: Git

Commit and push consolidated test reports directly to a dedicated branch or folder within your repository.

---

## 🏗️ Commit Flow

```mermaid
graph LR
    A[Reports Dir] --> B[Git Add]
    B --> C[Git Commit]
    C --> D[Git Push]
```

---

## 🛠️ Inputs

| Input | Default | Purpose |
| :--- | :--- | :--- |
| `run-id` | `REQUIRED`| Source workflow ID. |
| `branch` | `REQUIRED`| Target git branch. |
| `upload-reports` | `true` | Process XML results. |

---

## 🚀 Advanced Commits

### 🔄 Automatic Sync
This action is ideal for keeping a "latest" documentation folder in sync with the actual results from the main branch.

---

## 🆘 Troubleshooting

### ❌ Git Conflict
**Issue**: Pushes fail due to remote changes.
**Solution**: This action uses a force-push strategy on designated reporting branches to ensure visibility is always current.

---
[View Source Code](https://github.com/carlos-camara/qa-hub-actions/tree/main/upload-results)
