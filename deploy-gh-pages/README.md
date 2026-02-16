# 📂 Deploy to GitHub Pages

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Builds a Node.js project and deploys it to GitHub Pages. Perfect for documentation or dashboard sites.

## ⚡ Quick Info

- **Category**: Reporting & Notifications
- **Complexity**: Low
- **Version**: v1.2.0

## 🚀 Usage

```yaml
- name: Deploy Wiki
  uses: carlos-camara/qa-hub-actions/deploy-gh-pages@main
  with:
    dist-dir: "site/"
    build-command: "mkdocs build"
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `node-version` | Node.js version. | `'20'` |
| `install-command` | Command to install dependencies. | `'npm ci'` |
| `build-command` | Command to build the project. | `'npm run build'` |
| `dist-dir` | Directory containing build artifacts. | `'./dist'` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/deploy-gh-pages/)
