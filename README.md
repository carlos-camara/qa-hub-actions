<p align="center">
  <img src="https://socialify.git.ci/qa-hub/qa-hub-actions/image?description=1&font=Inter&language=1&name=1&owner=1&pattern=Circuit%20Board&theme=Dark" alt="QA Hub Actions" width="640" height="320" />
</p>

<p align="center">
  <a href="https://github.com/qa-hub/qa-hub-actions/actions"><img src="https://img.shields.io/github/actions/workflow/status/qa-hub/qa-hub-actions/lint.yml?style=for-the-badge&logo=github&label=Actionlint" alt="Workflow Status"></a>
  <a href="https://github.com/qa-hub/qa-hub-actions/releases"><img src="https://img.shields.io/github/v/release/qa-hub/qa-hub-actions?style=for-the-badge&color=blue" alt="Latest Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/qa-hub/qa-hub-actions?style=for-the-badge&color=green" alt="License"></a>
</p>

---

# 🛠 QA Hub Actions

Welcome to the core automation engine of **QA Hub**. This repository contains a collection of professional-grade, reusable GitHub Actions designed to bring consistency, speed, and deep visibility to your testing pipelines.

## 📦 Available Actions

| Action | Icon | Description |
| :--- | :---: | :--- |
| **[Setup Environment](./setup-environment)** | 🚀 | Multi-runtime (Node/Python) setup with smart caching. |
| **[Run QA Test Suite](./run-tests)** | 🧪 | Unit, API, GUI, and Performance test execution engine. |
| **[Collect & Publish](./collect-and-publish)** | 📊 | Aggregation of reports and PR-integrated summaries. |
| **[Slack Notification](./slack-notify)** | 📢 | Rich, formatted test status updates to Slack. |
| **[Perf Baseline](./performance-baseline-check)** | 📉 | Regression detection against performance baselines. |

## 🚀 Getting Started

To use these actions in your workflow, simply reference them using the standard GitHub Action syntax:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # 1. Setup
      - uses: qa-hub/qa-hub-actions/setup-environment@v1
        with:
          node-version: '20'

      # 2. Execute
      - uses: qa-hub/qa-hub-actions/run-tests@v1
        with:
          test-command-api: "npm run test:api"

      # 3. Report
      - uses: qa-hub/qa-hub-actions/collect-and-publish@v1
        if: always()
        with:
          api-reports-path: "results/api"
```

## 💎 Why QA Hub Actions?

- **Zero Boilerplate**: Pre-configured defaults for common QA patterns.
- **Deep Visibility**: Automatic generation of beautiful Job Summaries.
- **Fast Execution**: Built-in caching for both Node.js and Python ecosystems.
- **Composable**: Use one, a few, or all actions based on your needs.

---

<p align="center">
  Built by the <b>Carlos Cámara</b>
</p>
