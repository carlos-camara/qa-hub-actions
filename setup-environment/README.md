# 🚀 Setup QA Environment

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**Standardized, cached environment setup for Python and Node.js testing stacks.**

</div>

---

## 🚀 Overview

This action eliminates the boilterplate of setting up test environments. It handles caching, language versioning, and dependency installation for both Node.js and Python runtimes in a single, clean step.

### Key Features
- **🐍 Multi-Runtime**: setup Node.js and Python independently or together.
- **⚡ Smart Caching**: Automatically configured cache for `npm` and `pip`.
- **🔧 Custom Install**: Supports custom installation commands or defaults to `npm ci`/`pip install -r requirements.txt`.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/setup-environment@v1
  with:
    node-version: '20'
    python-version: '3.11'
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `node-version` | Node.js version. Empty to skip. | No | `''` |
| `python-version` | Python version. Empty to skip. | No | `''` |
| `node-install-command` | Custom Node install command. | No | `npm install` |
| `python-install-command` | Custom Python install command. | No | `pip install ...` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
