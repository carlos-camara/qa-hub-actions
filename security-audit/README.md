# <div align="center">🛡️ Action: Security Audit</div>

<div align="center">
  <p><i>Surgical protection for your codebase by scanning dependencies for vulnerabilities and performing static security analysis on Python code.</i></p>
</div>


---

## 🚀 Key Impact

- **🔒 Dependency Shield**: Scans your `requirements.txt` via `Safety` to detect known vulnerabilities in third-party packages.
- **🔍 Static Analysis**: Performs deep security audits of your Python source code using `Bandit` to identify common security smells.
- **⚖️ Configurable Audits**: Skip specific audit rules or toggle between dependency and code scans independently.
- **🛡️ Shift Left Security**: Catches critical security flaws during the CI process before they reach production environments.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `python-version` | No | `3.11` | Python runtime version to use for auditing. |
| `target-path` | No | `.` | Directory or file path to scan for code security. |
| `scan-dependencies` | No | `true` | Whether to perform `Safety` dependency checks. |
| `scan-code` | No | `true` | Whether to perform `Bandit` static analysis. |
| `bandit-skip` | No | - | Comma-separated list of Bandit IDs to ignore. |

---

## ⚡ Quick Start

```yaml
- name: 🛡️ Security Audit
  uses: carlos-camara/qa-hub-actions/security-audit@v1
  with:
    target-path: "app/"
    scan-dependencies: "true"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/security-audit/)
</div>
