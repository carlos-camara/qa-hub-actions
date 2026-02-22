# 📉 Action: PR Churn Analyzer

<div align="center">
  <p><i>Surgical detection of Technical Debt by comparing Logic vs Test changes.</i></p>
</div>

---

> [!IMPORTANT]  
> High-velocity engineering teams can accrue technical debt when core logic is modified without reciprocal test coverage. The **PR Churn Analyzer** monitors this ratio and automatically flags Pull Requests that introduce significant logic changes with insufficient testing.

## 🚀 Quick Start

Drop this snippet into your PR intelligence workflow:

```yaml
steps:
  - name: 📉 Analyze Code Churn & Test Debt
    uses: carlos-camara/qa-hub-actions/pr-churn-analyzer@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      logic-path: 'src/'
      test-path: 'tests/'
      debt-threshold-logic: '100'
      debt-threshold-tests: '10'
```

## ⚙️ Configuration

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `github-token` | Your `GITHUB_TOKEN` for API authentication. | **Yes** | N/A |
| `logic-path` | Path pattern identifying core application logic. | No | `features/steps/` |
| `test-path` | Path pattern identifying test files. | No | `.feature` |
| `debt-threshold-logic` | Lines of Code (LOC) added to logic that triggers a debt check. | No | `50` |
| `debt-threshold-tests` | Minimum Test LOC required if Logic LOC exceeds the threshold. | No | `5` |

## 🧬 How it works

1. It analyzes the PR diff to calculate the total Lines of Code (LOC) added to files matching `logic-path`.
2. It calculates the LOC added to files matching `test-path`.
3. If the ratio exceeds the configured thresholds (e.g., adding 50 lines of logic but fewer than 5 lines of tests), the system automatically flags the PR with a **Test Debt Warning** comment.
