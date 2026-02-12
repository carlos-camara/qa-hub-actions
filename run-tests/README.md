# 🧪 Action: Run QA Test Suite

The unified core engine for test orchestration, now with intelligent report organization.

## 📖 What it does
- **Service Orchestration**: Starts background services and waits for health checks.
- **Parallel Engines**: Runs API, GUI, and Performance tests standardized as a single run.
- **Intelligent Reporting**: Automatically organizes JUnit XML results into timestamped, project-specific folders (e.g., `reports/test_run/dashboard_2026-02-12_11-16-47/`).
- **Service Isolation**: Handles environment variables for headless browsers and standardizes output.

## 🛠️ Configuration

| Input | Required | Description |
| :--- | :--- | :--- |
| `test-command-api` | No | Command for API tests. If provided, API tests will run. |
| `test-command-gui` | No | Command for GUI tests. If provided, GUI tests will run. |
| `test-command-performance` | No | Command for Performance tests. |
| `project-name` | No | Name of the project (default: `dashboard`). Used for folder naming. |
| `headless` | No | Default `true`. |
| `enable-coverage`| No | Collect Pytest coverage. |

> [!IMPORTANT]
> **Dynamic Report Paths**: The action automatically injects the `--junit-dir` argument into your test commands to ensure all reports from the same run are consolidated into a unique timestamped folder.

## 🚀 Quick Start

```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@main
  with:
    project-name: "ciber"
    test-command-api: "qa-hub run --tags api"
    test-command-gui: "qa-hub run --tags gui"
```

---
[View full documentation →](https://carlos-camara.github.io/qa-hub-actions/actions/run-tests/)
