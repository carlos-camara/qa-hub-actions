# 🧪 Action: Run QA Test Suite

The unified core engine for test orchestration.

## 📖 What it does
- **Service Orchestration**: Starts background services and waits for health checks.
- **Parallel Engines**: Runs API, GUI, and Performance tests simultaneously or sequentially.
- **Service Isolation**: Handles environment variables for headless browsers and standardizes output.

## 🛠️ Configuration

| Input | Required | Description |
| :--- | :--- | :--- |
| `test-command-api` | No | Command for API tests. If provided, API tests will run. |
| `test-command-gui` | No | Command for GUI tests. If provided, GUI tests will run. |
| `test-command-performance` | No | Command for Performance tests. If provided, Performance tests will run. |
| `headless` | No | Default `true`. |
| `enable-coverage`| No | Collect Pytest coverage. |

> [!TIP]
> **Simplified Execution**: You no longer need to pass boolean flags like `run-api: true`. The action now automatically detects which tests to run based on the presence of the corresponding test command.

## 🚀 Quick Start

```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@v1
  with:
    test-command-api: "pytest tests/"
    enable-coverage: 'true'
    coverage-module: "qa_framework"
```

---
[View full documentation →](https://carlos-camara.github.io/qa-hub-actions/actions/run-tests/)
