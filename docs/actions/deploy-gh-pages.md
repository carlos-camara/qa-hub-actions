# 📂 Deploy to GH Pages

!!! info "At a Glance"
    - **Category**: Reporting & Notifications
    - **Complexity**: Low
    - **Version**: v1.2.0 (Stable)
    - **Primary Tool**: actions/deploy-pages / Vite

Publish your documentation or HTML test reports to GitHub Pages with a single step.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `node-version` | Node.js version to use. | `'20'` |
| `install-command` | Command to install dependencies. | `'npm ci'` |
| `build-command` | Command to build the project. | `'npm run build'` |
| `dist-dir` | Directory containing build artifacts. | `'./dist'` |
| `vite-api-url` | `VITE_API_URL` environment variable. | `""` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/deploy-gh-pages@main
  with:
    dist-dir: "site/"
    build-command: "mkdocs build"
```

---
*Share your results with the world.*
