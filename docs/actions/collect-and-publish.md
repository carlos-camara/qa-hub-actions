# 📊 Collect & Publish

!!! info "At a Glance"
    - **Category**: Core Engine
    - **Complexity**: Medium
    - **Version**: v1.0.5 (Stable)
    - **Primary Tool**: GitHub PR Comments / Artifacts

Aggregate test results and generate a premium reporting summary directly in your Pull Request.

## 📖 Overview

This action scans your repository for test results (JUnit XML, JSON, etc.), aggregates them into a unified report, and posts a high-fidelity summary as a PR comment.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `reports-path` | Directory where test reports are stored. | `""` |
| `github-token` | Token for posting PR comments. | `${{ github.token }}` |
| `artifact-name` | Name for the stored artifact. | `"test-reports"` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/collect-and-publish@main
  if: always()
  with:
    reports-path: "results/test_run"
```

---
*Transform data into actionable insights.*
