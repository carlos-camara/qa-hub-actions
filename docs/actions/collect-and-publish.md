# 📊 Collect & Publish

!!! info "At a Glance"
    - **Category**: Core Engine
    - **Complexity**: Medium
    - **Version**: v1.0.5 (Stable)
    - **Primary Tool**: GitHub PR Comments / Artifacts

Aggregate test results and generate a premium reporting summary directly in your Pull Request.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `reports-path` | Path to test reports directory (API/GUI). | `""` |
| `screenshots-path` | Path/Pattern for screenshots (e.g., `screenshots/*.png`). | `""` |
| `performance-reports-path` | Path to performance reports directory. | `""` |
| `junit-results-dir` | Directory where all JUnit XMLs will be aggregated. | `junit-results` |
| `upload-artifacts` | Whether to upload artifact reports. | `true` |
| `publish-results` | Whether to publish the test reporter summary. | `true` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/collect-and-publish@main
  if: always()
  with:
    reports-path: "results/test_run"
    screenshots-path: "features/resources/screenshots/*.png"
    upload-artifacts: 'true'
```

---
*Transform data into actionable insights.*
