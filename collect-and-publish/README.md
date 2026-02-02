# 📊 Collect and Publish QA Results

Aggregates test results, uploads artifacts, and publishes visual summaries to GitHub Job Summaries and PRs.

## 🛠 Features

- **JUnit Aggregation**: Collects XML results from multiple paths into a single directory.
- **Artifact Management**: Uploads API reports, GUI reports, and screenshots automatically.
- **Interactive Summaries**: Generates a clean markdown table in the GitHub Job Summary.
- **PR Integration**: Publishes detailed test reports using `dorny/test-reporter`.

## 📥 Inputs

| Name | Description | Default |
| :--- | :--- | :--- |
| `api-reports-path` | Path to API reports. | `""` |
| `gui-reports-path` | Path to GUI reports. | `""` |
| `screenshots-path` | Path/Pattern for screenshots. | `""` |
| `performance-reports-path`| Path to performance reports. | `""` |
| `junit-results-dir` | Directory for aggregated JUnit XMLs. | `junit-results` |
| `upload-artifacts` | Whether to upload artifact reports. | `true` |
| `publish-results` | Publish the test reporter summary. | `true` |

## 🚀 Usage

```yaml
- uses: qa-hub-actions/collect-and-publish@v1
  if: always()
  with:
    api-reports-path: "reports/api"
    gui-reports-path: "reports/gui"
```
