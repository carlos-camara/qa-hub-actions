# 📊 Collect and Publish QA Results

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**Aggregate test reports, upload artifacts, and publish summaries directly to Pull Requests.**

</div>

---

## 🚀 Overview

This action serves as the central reporting hub for your testing pipeline. It aggregates JUnit XML reports from various test sources (API, GUI, Performance), uploads them as build artifacts for later analysis, and publishes a comprehensive summary to the GitHub Actions job summary and PR comments.

### Key Features
- **📂 Artifact Aggregation**: Collects reports from scattered directories into a single artifact.
- **📝 PR Integration**: Publishes a detailed test summary directly to the PR.
- **🛡️ Always-On Mode**: Designed to run even if tests fail (`if: always()`).

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/collect-and-publish@v1
  if: always() # Important!
  with:
    reports-path: 'reports/unified'
    screenshots-path: 'reports/screenshots/*.png'
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `reports-path` | Path to directory containing test JUnit XML reports (API/GUI). | No | `''` |
| `performance-reports-path` | Path to directory containing Performance reports. | No | `''` |
| `screenshots-path` | Glob pattern for screenshots to upload (e.g., `screenshots/*.png`). | No | `''` |
| `junit-results-dir` | Directory where all XMLs are aggregated before publishing. | No | `junit-results` |
| `upload-artifacts` | Set to `false` to disable artifact uploading. | No | `true` |
| `publish-results` | Set to `false` to disable PR comment publishing. | No | `true` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
