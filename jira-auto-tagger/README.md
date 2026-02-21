# 🏷️ Jira Auto-Tagger Action

<div align="center">

[![GitHub Action](https://img.shields.io/badge/GitHub-Action-2088FF?logo=github-actions&logoColor=white)](https://github.com/carlos-camara/qa-hub-actions)
[![Jira](https://img.shields.io/badge/Jira-Integration-0052CC?logo=jira&logoColor=white)](https://github.com/carlos-camara/qa-hub-actions)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://github.com/carlos-camara/qa-hub-actions)

*Seamlessly synchronize your QA test scenarios with Jira project management.*

</div>

---

## 📖 Overview

The **Jira Auto-Tagger** action intelligently scans your repository for Gherkin `.feature` files. 
If it finds any features or scenarios without a Jira tracking ID, it automatically connects to your Jira instance to build a pristine BDD Agile Board. 
It creates a new `Tarea` (Task) for the Feature itself (extracting its description), and creates `Subtarea` (Sub-tasks) for each Scenario, securely committing the tags (e.g., `@CC-123`) back to your codebase.

Designed for **maximum reliability**, it works safely even in detached HEAD environments (like PR builds) using an `autostash` rebase push logic, ensuring your codebase always accurately reflects your Jira board.

---

## ✨ Features

- **🏢 Native Jira Hierarchy**: Automatically structures your Agile Board using the BDD standard: Epic (Test Plan) > Task (Feature) > Sub-task (Scenario).
- **📋 Context Extraction**: Automatically parses the massive descriptive text blocks under your `Feature:` keyword in Gherkin and injects them as the Jira Task description.
- **🧠 Intelligent Tag Parsing**: Detects existing Jira tags spread across multiple lines to avoid duplicate ticket creation.
- **🪄 Inline Injection**: Keeps your Gherkin clean by prepending new Jira tags on the exact same line as your existing tags.
- **🔄 Bidirectional Sync**: Creates the ticket in Jira and immediately documents the ID in GitHub.
- **🛡️ Bulletproof Commits**: Safely handles unstaged changes in CI runners (like `package-lock.json` modifications) before pushing.
- **📈 Historical Execution Tracking**: Manages a rolling maximum 10-run execution table inside the Jira Issue description, preventing comment pollution while providing instant traceability.
- **🚥 Kanban Telemetry**: Automatically transitions Jira workflows (e.g., to PASSED/FAILED) based on the latest pipeline results.

---

## ⚙️ Inputs

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `jira-url` | Base URL of your Jira instance (*e.g., `https://yourdomain.atlassian.net`*) | **Yes** | - |
| `jira-user` | Jira account email/username used for API authentication | **Yes** | - |
| `jira-token` | Atlassian API Token | **Yes** | - |
| `jira-project-key` | Key of the Jira project to create tasks in (*e.g., SCRUM, CC*) | **Yes** | - |
| `jira-parent-plan` | Optional Issue Key of a parent Test Plan to link scenarios to (*e.g., CC-10*) | No | - |
| `features-dir` | Target directory to scan for `.feature` files | No | `features` |

---

## 🚀 Usage

Integrate the Auto-Tagger into your pipeline **before** your test execution step. This guarantees that your test runner processes the newly tagged feature files and can report their execution status back to Jira.

```yaml
jobs:
  test-and-tag:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout Code
        uses: actions/checkout@v4
        
      # ... environment setup ...

      - name: 🏷️ Auto-Tag Gherkin Scenarios with Jira IDs
        uses: carlos-camara/qa-hub-actions/jira-auto-tagger@main
        with:
          jira-url: ${{ secrets.JIRA_URL }}
          jira-user: ${{ secrets.JIRA_USER }}
          jira-token: ${{ secrets.JIRA_API_TOKEN }}
          jira-project-key: "CC"

      - name: 🧪 Execute Tests
        uses: carlos-camara/qa-hub-actions/run-tests@main
        with:
          test-command-api: "qa-hub run --env staging --tags api"
          # ... rest of your testing logic ...
```

---

<div align="center">
  <i>Part of the QA Hub Actions Core Framework</i>
</div>
