# 📂 Deploy to GH Pages

Publish your documentation or HTML test reports to GitHub Pages with a single step.

## 📖 Overview

Standardizes the deployment of static files to the `gh-pages` branch. It handles authentication and directory cleaning automatically.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `publish-dir` | Directory containing the static site. | `'docs-site'` |
| `github-token` | Token with write permissions. | `${{ github.token }}` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/deploy-gh-pages@main
  with:
    publish-dir: "site/"
```

---
*Share your results with the world.*
