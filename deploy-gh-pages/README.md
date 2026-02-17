# 📂 Action: Deploy to GitHub Pages

Effortlessly host your QA dashboards, documentation wikis, and static reports on GitHub Pages with automated builds and SPAs support.

---

## 🚀 Key Impact

- **📦 Multi-Runtime Support**: Pre-configured for Node.js environments with customizable install and build commands.
- **🌍 SPA Ready**: Automatically handles `.nojekyll` and `404.html` redirection for modern frontend frameworks (e.g., Vite, React).
- **⚡ Surgical Caching**: Built-in support for `npm` caching to accelerate deployment cycles.
- **🔐 Secure Deployment**: Utilizes official GitHub Action primitives for trusted, authenticated deployments.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `node-version` | No | `20` | Node.js runtime version. |
| `install-command` | No | `npm ci` | Command to install dependencies. |
| `build-command` | No | `npm run build` | Command to generate the static site. |
| `dist-dir` | No | `./dist` | Directory containing the assets to deploy. |
| `vite-api-url` | No | - | Optional `VITE_API_URL` environment variable. |

---

## ⚡ Quick Start

```yaml
- name: 📂 Deploy Documentation Wiki
  uses: carlos-camara/qa-hub-actions/deploy-gh-pages@main
  with:
    dist-dir: "site/"
    build-command: "mkdocs build"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/deploy-gh-pages/)
</div>
