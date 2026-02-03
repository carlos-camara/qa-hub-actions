# 🛡️ Action: Security Audit

Automated security shield for Python automation projects.

## 📖 What it does
- **Dependency Shield**: Scans `requirements.txt` via `Safety`.
- **Static Analysis**: Identifies security smells via `Bandit`.
- **Shift Left**: Catches vulnerabilities before they reach production.

## 🛠️ Configuration

| Input | Default | Description |
| :--- | :---: | :--- |
| `target-path` | `"."` | Path to scan with Bandit. |
| `python-version`| `'3.11'` | Python version to use. |

## 🚀 Quick Start

```yaml
- uses: carlos-camara/qa-hub-actions/security-audit@v1
  with:
    target-path: "qa_framework/"
```

---
[View full documentation →](https://carlos-camara.github.io/qa-hub-actions/actions/security-audit/)
