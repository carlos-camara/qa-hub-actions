# ⚙️ Action: Setup Environment

Smart multi-runtime preparation with automatic caching.

## 📖 What it does
- **Multi-Runtime Suport**: Configures Python and Node.js in a single step.
- **Smart Caching**: Optimizes `npm` and `pip` caching based on lock files.
- **Stability**: Ensures a clean, consistent environment for every test run.

## 🛠️ Configuration

| Input | Default | Description |
| :--- | :---: | :--- |
| `node-version` | `'20'` | Version of Node.js. |
| `python-version` | `'3.11'` | Version of Python. |
| `cache` | `'true'` | Toggle caching. |

## 🚀 Quick Start

```yaml
- uses: carlos-camara/qa-hub-actions/setup-environment@v1
  with:
    node-version: '20'
    python-version: '3.12'
```

---
[View full documentation →](https://carlos-camara.github.io/qa-hub-actions/actions/setup-environment/)
