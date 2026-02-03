# 🛡️ Security Audit

/// details | At a Glance
- **Category**: Quality & Security
- **Version**: v1.0.0 (New)
- **Primary Tool**: Safety / Bandit
- **Best Practice**: Run on every PR
///

Automated vulnerability scanning for Python dependencies and static code analysis.

## 📖 Overview

The `security-audit` action combines `Safety` (dependency vulnerability check) and `Bandit` (static code analysis) to ensure your automation code follows security best practices.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `target-path` | Directory to scan with Bandit. | `"."` |
| `python-version` | Python version for the audit. | `'3.11'` |
| `scan-dependencies` | Whether to check dependencies. | `'true'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/security-audit@main
  with:
    target-path: "qa_framework/"
```

---
*Security is not a feature, it's a foundation.*
