# 🧪 Run QA Test Suite

!!! info "At a Glance"
    - **Category**: Core Engine
    - **Complexity**: High
    - **Version**: v1.2.0 (Stable)
    - **Primary Tool**: Pytest / Behave / Locust

The unified execution engine for all your testing needs. High-concurrency support, service health checks, and standardized reporting.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `start-services-command` | Command to start background services (e.g., `npm start &`). | `""` |
| `health-check-urls` | Space-separated URLs to wait for (e.g., `http://localhost:3000`). | `""` |
| `test-command-api` | Command for API tests (e.g., `npm run test:api`). | `""` |
| `test-command-performance` | Command for Performance tests (e.g., `locust -f locustfile.py`). | `""` |
| `test-command-gui` | Command for GUI tests (e.g., `npm run test:gui`). | `""` |
| `run-api` | Whether to run API tests. | `true` |
| `run-performance` | Whether to run performance tests. | `true` |
| `run-gui` | Whether to run GUI tests. | `true` |
| `headless` | Run GUI tests in headless mode. | `true` |
| `enable-coverage` | Whether to collect code coverage (using Pytest). | `false` |
| `coverage-module` | Module to collect coverage for. | `""` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@main
  with:
    start-services-command: "npm start &"
    health-check-urls: "http://localhost:3000"
    test-command-api: "pytest tests/"
    enable-coverage: 'true'
    coverage-module: "qa_framework"
```

---
*Built for speed and reliability.*
