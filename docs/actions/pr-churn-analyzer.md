# 📉 Action: PR Churn Analyzer

<div align="center">
  <p><i>Surgical detection of Technical Debt by comparing Logic vs Test changes.</i></p>
</div>

---

> [!IMPORTANT]  
> High-velocity engineering teams can accrue technical debt when core logic is modified without reciprocal test coverage. The **PR Churn Analyzer** monitors this ratio and automatically flags Pull Requests that introduce significant logic changes with insufficient testing.

## 🚀 Key Impact

- **📉 Debt Visualization**: Mathematically detects if testing parity is lagging behind logic changes.
- **🚦 Quality Gates**: Safeguards against "test-less" feature growth in critical modules.
- **🧠 Automated Review**: Highlights risky PRs for senior architectural intervention.

---

## ⚙️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | Your `GITHUB_TOKEN` for API authentication. |
| `logic-path` | No | `features/steps/` | Path pattern identifying core application logic. |
| `test-path` | No | `.feature` | Path pattern identifying test files. |
| `debt-threshold-logic` | No | `50` | Logic LOC threshold to trigger check. |
| `debt-threshold-tests` | No | `5` | Minimum Test LOC required. |

---

## ⚡ Quick Start

```yaml
- name: 📉 Analyze Code Churn & Test Debt
  uses: carlos-camara/qa-hub-actions/pr-churn-analyzer@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    logic-path: 'src/'
    test-path: 'tests/'
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-churn-analyzer/)
</div>
