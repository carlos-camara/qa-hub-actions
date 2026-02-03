# 📊 Action: Collect & Publish

Unified reporting and PR integrated test summaries.

## 📖 What it does
- **Aggregation**: Scans for JUnit XML and JSON reports.
- **PR Integration**: Posts a high-fidelity summary comment in Pull Requests.
- **Artifact Management**: Stores reports for historical analysis.

## 🛠️ Configuration

| Input | Default | Description |
| :--- | :---: | :--- |
| `reports-path` | `REQUIRED` | Path to generated reports. |
| `artifact-name` | `"test-reports"` | GitHub Artifact name. |

## 🚀 Quick Start

```yaml
- uses: carlos-camara/qa-hub-actions/collect-and-publish@v1
  if: always()
  with:
    reports-path: "results"
```

---
[View full documentation →](https://carlos-camara.github.io/qa-hub-actions/actions/collect-and-publish/)
