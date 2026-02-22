# 🤖 PR Risk Analyzer Action

Protects your project by scanning Pull Requests for changes in critical files or directories. If a critical file is modified, the action:
1. Adds a glaring red `high-risk` label to the PR.
2. Injects an aggressive Github Caution Alert `[!CAUTION]` block at the very top of the PR description to ensure reviewers pay extreme attention.

## 🚀 Usage

```yaml
steps:
  - name: 📥 Checkout Repository
    uses: actions/checkout@v6
    with:
      fetch-depth: 0 # Required to compare against the base branch

  - name: 🤖 Perform Risk Analysis
    uses: carlos-camara/qa-hub-actions/pr-risk-analyzer@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      # Optional: Override the default critical patterns (space-separated)
      critical-patterns: 'server.js services/db.js .github/workflows/ package.json package-lock.json nginx.conf'
```
