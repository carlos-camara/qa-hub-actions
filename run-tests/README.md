# 🧪 Action: Run QA Test Suite

The unified core engine for test orchestration, featuring industrial-grade report consolidation and multi-engine support for API, GUI, and Performance tests.

---

## 🚀 Key Impact

- **🏗️ Industrial Orchestration**: Executes API, GUI, and Performance test suites with standardized control.
- **📊 Intelligent Reporting**: Automatically organizes JUnit XML results into timestamped, project-specific directories.
- **🔄 Surgical Isolation**: Injects dynamic report paths into test engines to prevent cross-run collisions.
- **🩺 Health Integration**: Built-in support for starting background services and performing pre-flight health checks.
- **🤝 Jira Test Reporting**: Automatically reports test execution results into Jira Tasks, transitioning their status and updating an ongoing Markdown History Table inside the Jira issue's description (use alongside `jira-auto-tagger` for end-to-end sync).
- **📝 Execution Logs Injection**: Automatically extracts `<system-out>` execution logs (the exact steps run by Behave/Pytest) and injects them directly into the Jira issue description for instant debugging visibility.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `test-command-api` | No | - | Command for API tests (e.g., `pytest`). |
| `test-command-gui` | No | - | Command for GUI tests (e.g., `playwright`). |
| `test-command-performance`| No | - | Command for Performance tests (e.g., `locust`).|
| `project-name` | No | `dashboard` | Project identifier used for report folder naming. |
| `headless` | No | `true` | Run GUI tests in headless mode. |
| `enable-coverage` | No | `false` | Whether to collect and report code coverage. |
| `jira-sync` | No | `false` | Enable auto-tagging of scenarios and reporting results to Jira. |
| `jira-url` | No | - | Your Jira domain. |
| `jira-user` | No | - | Email address used for Jira authentication. |
| `jira-token` | No | - | Jira API Token for authentication. |
| `jira-project-key` | No | `DAS` | The Jira Project Key where UI tests should be managed. |
| `jira-test-status-field` | No | - | Name of a Custom Jira Field for status (optional, defaults to History Table). |

> [!IMPORTANT]
> **Dynamic Pathing & Tracking**: This action automatically appends `--junit-dir` to your test commands to ensure results are archived. With Jira Sync enabled, it parses the XML and injects an **ADF Execution Table** and **Execution Logs** into your Agile boards.

---

## ⚡ Quick Start

### Basic Usage
```yaml
- name: 🧪 Run Quality Suites
  uses: carlos-camara/qa-hub-actions/run-tests@main
  with:
    project-name: "core-api"
    test-command-api: "pytest tests/api"
    test-command-gui: "pytest tests/gui"
```

### Advanced Usage with Jira End-to-End Sync
```yaml
- name: 🏷️ Auto-Tag Gherkin Scenarios with Jira IDs
  uses: carlos-camara/qa-hub-actions/jira-auto-tagger@main
  with:
    jira-url: ${{ secrets.JIRA_URL }}
    jira-user: ${{ secrets.JIRA_USER }}
    jira-token: ${{ secrets.JIRA_API_TOKEN }}
    jira-project-key: "CC"

- name: 🧪 Run Quality Suites & Report to Jira
  uses: carlos-camara/qa-hub-actions/run-tests@main
  with:
    project-name: "dashboard"
    test-command-gui: "qa-hub run --tags gui"
    jira-sync: "true"
    jira-url: ${{ secrets.JIRA_URL }}
    jira-user: ${{ secrets.JIRA_USER }}
    jira-token: ${{ secrets.JIRA_API_TOKEN }}
    jira-project-key: "CC"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/run-tests/)
</div>
