# 🧪 Action: Run QA Test Suite

The unified core engine for test orchestration.

## 📖 What it does
- **Service Orchestration**: Starts background services and waits for health checks.
- **Parallel Engines**: Runs API, GUI, and Performance tests simultaneously or sequentially.
- **Service Isolation**: Handles environment variables for headless browsers and standardizes output.

## 🛠️ Configuration

| Input | Required | Description |
| :--- | :---: | :--- |
| `test-command-api` | No | Command for API tests. |
| `test-command-gui` | No | Command for GUI tests. |
| `headless` | No | Default `true`. |
| `enable-coverage`| No | Collect Pytest coverage. |

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
