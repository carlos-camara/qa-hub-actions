# 🧪 Run QA Test Suite

!!! info "At a Glance"
    - **Category**: Core Engine
    - **Complexity**: High
    - **Recent Version**: v1.2.0 (Stable)
    - **Primary Tool**: Pytest / Behave / Locust

The unified execution engine for all your testing needs. High-concurrency support, service health checks, and standardized reporting stashing.

---

## 🏗️ Architecture

```mermaid
graph TD
    A[Action Triggered] --> B{Start Services?}
    B -- Yes --> C[Run start-services-command]
    B -- No --> D{Health Check?}
    C --> D
    D -- Yes --> E[Wait for health-check-urls]
    D -- No --> F[Execute Tests]
    E --> F
    F --> G[Stash Reports]
    G --> H[Action Completed]
```

---

## 🛠️ Configuration Details

| Input | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `start-services-command` | `String` | `""` | Command to start your app (e.g., `npm start &`). |
| `health-check-urls` | `String` | `""` | Space-separated URLs to wait for (e.g., `http://localhost:3000`). |
| `test-command-api` | `String` | `""` | Command for API tests (e.g., `pytest tests/api`). |
| `test-command-gui` | `String` | `""` | Command for GUI tests (e.g., `npm run test:gui`). |
| `enable-coverage` | `Boolean`| `false`| Whether to collect code coverage. |

---

## 🚀 Advanced Usage

### 📊 Coverage Mapping
When `enable-coverage` is set to `true`, the action automatically wraps your command with `pytest --cov`.

```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@v1
  with:
    test-command-api: "pytest tests/"
    enable-coverage: 'true'
    coverage-module: "app_logic"
```

### 🖱️ GUI Headless Control
Toggle between headless and headed execution using the `headless` parameter.

```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@v1
  with:
    test-command-gui: "behave features/"
    headless: 'false'  # Set to false for debugging
```

---

## 🆘 Troubleshooting

### ❌ Health check timeout
**Issue**: The action fails during the "Wait for Services" step.
**Solution**: 
1. Increase the timeout in your app's startup or verify the `health-check-urls` are correct.
2. Ensure you backgrounded your app (e.g., using `&` in Linux).

### 🔍 Missing Reports
**Issue**: Tests pass but reports are not stashed.
**Solution**: Standardize your test command to output to a folder named `reports`.

---
[View Source Code](https://github.com/carlos-camara/qa-hub-actions/tree/main/run-tests)
