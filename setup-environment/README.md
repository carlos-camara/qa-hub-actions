# 🚀 Setup QA Environment

This action provides a standardized way to set up Python and Node.js environments for QA projects. It includes automatic caching and supports custom installation commands.

## 🛠 Features

- **Multi-Runtime Support**: Configure Python, Node.js, or both.
- **Smart Caching**: integrated `actions/setup-python` and `actions/setup-node` caching for faster runs.
- **Customizable**: Override default install commands for `pip` and `npm`.

## 📥 Inputs

| Name | Description | Default |
| :--- | :--- | :--- |
| `python-version` | Python version (e.g., `3.11`). Skip if empty. | `""` |
| `node-version` | Node.js version (e.g., `20`). Skip if empty. | `""` |
| `python-install-command` | Command for Python dependencies. | `python -m pip install ...` |
| `node-install-command` | Command for Node dependencies. | `npm install` |

## 🚀 Usage

```yaml
- uses: qa-hub-actions/setup-environment@v1
  with:
    python-version: '3.11'
    node-version: '20'
```
