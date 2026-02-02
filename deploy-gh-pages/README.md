# 🚀 Deploy to GitHub Pages

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**Build and deploy Node.js applications directly to GitHub Pages.**

</div>

---

## 🚀 Overview

A streamlined action to build your modern web application (React, Vue, Vite, etc.) and deploy it to GitHub Pages. It handles dependency installation, building, and artifact upload in a single step.

### Key Features
- **⚡ Fast Builds**: Uses `npm ci` and caching for optimal speed.
- **🔧 Configurable**: Supports custom build commands and output directories.
- **🔐 Secure**: Uses GitHub's native `actions/deploy-pages`.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/deploy-gh-pages@v1
  with:
    node-version: '20'
    build-command: 'npm run build'
    dist-dir: './dist'
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `node-version` | Node.js version to use for the build. | No | `20` |
| `install-command` | Command to install dependencies. | No | `npm ci` |
| `build-command` | Command to build the project. | No | `npm run build` |
| `dist-dir` | Directory containing the build output to deploy. | No | `./dist` |
| `vite-api-url` | Inject `VITE_API_URL` environment variable during build. | No | `''` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
