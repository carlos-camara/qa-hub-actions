# ⚙️ Setup Environment

!!! info "At a Glance"
    - **Category**: Core Engine
    - **Complexity**: Low
    - **Version**: v1.1.0 (Stable)
    - **Primary Tool**: actions/setup-python / actions/setup-node

One-stop configuration for multi-runtime QA projects. Automatic caching and dependency management.

## 📖 Overview

Standardizes the environment setup for both Python and Node.js. It automatically configures caching for `pip` and `npm`, ensuring your pipelines start as fast as possible.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `node-version` | Version of Node.js to install. | `'20'` |
| `python-version` | Version of Python to install. | `'3.11'` |
| `cache` | Enable/disable automatic caching. | `'true'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/setup-environment@main
  with:
    node-version: '20.x'
    python-version: '3.12'
```

---
*Consistent environments, faster builds.*
