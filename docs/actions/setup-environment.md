# ⚙️ Setup Environment

!!! info "At a Glance"
    - **Category**: Core Engine
    - **Complexity**: Low
    - **Version**: v1.1.0 (Stable)
    - **Primary Tool**: actions/setup-python / actions/setup-node

One-stop configuration for multi-runtime QA projects. Automatic caching and dependency management.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `python-version` | Python version to use (e.g., `3.11`). Leave empty to skip. | `""` |
| `node-version` | Node.js version to use (e.g., `20`). Leave empty to skip. | `""` |
| `python-install-command` | Command to install Python dependencies. | `python -m pip install --upgrade pip && if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi` |
| `node-install-command` | Command to install Node dependencies. | `if [ -f "package.json" ]; then npm install; fi` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/setup-environment@main
  with:
    node-version: '20'
    python-version: '3.12'
    python-install-command: "pip install -e ."
```

---
*Consistent environments, faster builds.*
