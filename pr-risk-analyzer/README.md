# 🤖 Action: PR Risk Analyzer

<div align="center">
  <p><i>Surgically protect your main branches by dynamically highlighting changes in mission-critical files.</i></p>
</div>

---

> [!CAUTION]
> The **PR Risk Analyzer** acts as a final safety net. It scans Pull Requests for modifications matching high-risk patterns (e.g., `package.json`, `server.js`, `nginx.conf`). If detected, it applies a glaring red `high-risk` label and injects an aggressive alert block at the top of the PR description to enforce executive review.

## 🚀 Quick Start

Drop this snippet into your PR intelligence workflow:

```yaml
steps:
  - name: 📥 Checkout Repository
    uses: actions/checkout@v6
    with:
      fetch-depth: 0 # Required for delta comparison

  - name: 🤖 Perform Risk Analysis
    uses: carlos-camara/qa-hub-actions/pr-risk-analyzer@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      critical-patterns: 'server.js services/db.js package.json' # Optional override
```

## ⚙️ Configuration

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `github-token` | Your `GITHUB_TOKEN` for API authentication to add labels and edit the PR description. | **Yes** | N/A |
| `critical-patterns` | Space-separated list of file/directory patterns that trigger a high-risk alert. | No | `.github/workflows/ package.json package-lock.json server.js nginx.conf` |
