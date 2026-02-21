# <div align="center">🐍 Action: Setup Environment</div>

<div align="center">
  <p><i>High-speed, multi-runtime preparation for Python and Node.js environments featuring intelligent dependency caching and custom installation logic.</i></p>
</div>


---

## 🚀 Key Impact

- **📦 Multi-Runtime Preparation**: Configures Python and Node.js runtimes in a single, surgical step.
- **⚡ Intelligent Caching**: Automatically manages `pip` and `npm` caches to reduce build times by up to 60%.
- **🛠️ Custom Installation**: Override default install commands to support complex dependency trees (Poetry, Yarn, pnpm).
- **🛡️ Environment Stability**: Ensures a consistent, clean environment for reliable test execution across all runners.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `python-version` | No | - | Python version to install (e.g., `3.11`). |
| `node-version` | No | - | Node.js version to install (e.g., `20`). |
| `python-install-command`| No | (Table) | Command to install Python dependencies. |
| `node-install-command` | No | (Table) | Command to install Node.js dependencies. |
| `python-cache` | No | `pip` | Cache strategy for Python: `pip`, `poetry`, etc. |
| `node-cache` | No | `npm` | Cache strategy for Node: `npm`, `yarn`, `pnpm`. |

---

## ⚡ Quick Start

```yaml
- name: 🐍 Prepare Environment
  uses: carlos-camara/qa-hub-actions/setup-environment@v1
  with:
    python-version: "3.11"
    node-version: "20"
    python-cache: "pip"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/setup-environment/)
</div>
