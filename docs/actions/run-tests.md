# 🧪 Run QA Test Suite

/// details | At a Glance
- **Category**: Core Engine
- **Complexity**: High
- **Version**: v1.2.0 (Stable)
- **Primary Tool**: Pytest / Behave / Locust
///

The unified execution engine for all your testing needs. High-concurrency support, service health checks, and standardized reporting.

## 📖 Overview

The `run-tests` action is designed to be the single entry point for test execution. It can handle background services, wait for them to be healthy, and run API, GUI, and Performance tests in a single step.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `test-command-api` | Command to run API tests. | `""` |
| `test-command-gui` | Command to run GUI tests. | `""` |
| `test-command-performance` | Command to run performance tests. | `""` |
| `run-api` | Whether to run API tests. | `true` |
| `run-gui` | Whether to run GUI tests. | `true` |
| `run-performance` | Whether to run performance tests. | `true` |
| `headless` | Run GUI tests in headless mode. | `true` |
| `enable-coverage` | Collect code coverage (Pytest). | `false` |
| `coverage-module` | Target module for coverage. | `""` |

## 🚀 Usage Example

### Running Pytest with Coverage
```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@main
  with:
    test-command-api: "pytest tests/"
    enable-coverage: 'true'
    coverage-module: "my_app"
```

### Running GUI Tests with Selenium
```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@main
  with:
    test-command-gui: "behave features/"
    headless: 'true'
```

---
*Built for speed and reliability.*
