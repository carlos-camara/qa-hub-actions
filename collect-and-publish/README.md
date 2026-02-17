# 📊 Action: Collect & Publish

Aggregate multi-engine test results, screenshots, and performance data into a high-fidelity visual summary directly in your Pull Requests.

---

## 🚀 Key Impact

- **🔄 Unified Aggregation**: Automatically merges JUnit XML results from API, GUI, and Performance test engines.
- **🖼️ Visual Evidence**: Uploads and organizes GUI screenshots as accessible GitHub artifacts.
- **📈 PR Intelligence**: Posts a comprehensive test summary to GitHub Actions and PR comments for instant visibility.
- **🛠️ Configurable Storage**: Toggle artifact uploads for reports, screenshots, and performance data independently.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `reports-path` | No | `""` | Path to the directory containing test reports. |
| `screenshots-path` | No | `""` | Glob pattern for screenshots (e.g., `results/*.png`). |
| `performance-reports-path`| No | `""` | Path to the directory containing performance data. |
| `junit-results-dir` | No | `junit-results` | Internal directory for merging JUnit XMLs. |
| `upload-artifacts` | No | `true` | Whether to save reports as GitHub artifacts. |
| `publish-results` | No | `true` | Whether to post the summary to the PR/Job summary. |

---

## ⚡ Quick Start

```yaml
- name: 📊 Collect & Publish Results
  uses: carlos-camara/qa-hub-actions/collect-and-publish@v1
  if: always()
  with:
    reports-path: "reports/"
    screenshots-path: "screenshots/**/*.png"
    publish-results: "true"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/collect-and-publish/)
</div>
