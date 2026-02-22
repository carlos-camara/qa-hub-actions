# 🤖 Action: PR Risk Analyzer

<div align="center">
  <p><i>Surgically protect your main branches by dynamically highlighting changes in mission-critical files.</i></p>
</div>

---

> [!CAUTION]
> The **PR Risk Analyzer** acts as a final safety net. It scans Pull Requests for modifications matching high-risk patterns (e.g., `package.json`, `server.js`). If detected, it applies a `high-risk` label and injects an alert block at the top of the PR.

## 🚀 Key Impact

- **🚨 Critical Watchlist**: Automatically monitors changes to core configuration, security, and infrastructure files.
- **🏷️ Automated Labeling**: Applies visual `high-risk` tags for immediate reviewer prioritization.
- **⚠️ Inline Warnings**: Injects aggressive feedback directly into the PR description to prevent accidental merges.

---

## ⚙️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | Token for labeling and patching descriptions. |
| `critical-patterns` | No | `.github/...` | Space-separated file patterns to watch. |

---

## ⚡ Quick Start

```yaml
- name: 🤖 Perform Risk Analysis
  uses: carlos-camara/qa-hub-actions/pr-risk-analyzer@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    critical-patterns: 'config/ migrations/ auth.js'
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-risk-analyzer/)
</div>
