# 🧪 Run QA Test Suite

The core execution engine for QA Hub. It handles service startup, health checks, and running multiple test types (API, GUI, Performance) in a unified way.

## 🛠 Features

- **Service Orchestration**: Start background services and wait for them to be healthy.
- **Parallel Test Discovery**: Run API, GUI, and Performance tests in one step.
- **Headless Mode**: Built-in support for headless browser testing.

## 📥 Inputs

| Name | Description | Default |
| :--- | :--- | :--- |
| `start-services-command` | Command to start services (e.g., `npm start &`). | `""` |
| `health-check-urls` | URLs to wait-on before testing. | `""` |
| `test-command-api` | Command for API tests. | `""` |
| `test-command-gui` | Command for GUI tests. | `""` |
| `test-command-performance`| Command for Performance tests. | `""` |
| `run-api` | Boolean toggle for API tests. | `true` |
| `run-gui` | Boolean toggle for GUI tests. | `true` |
| `run-performance` | Boolean toggle for Performance tests. | `true` |
| `headless` | Run GUI tests in headless mode. | `true` |

## 🚀 Usage

```yaml
- uses: qa-hub-actions/run-tests@v1
  with:
    start-services-command: "npm start &"
    health-check-urls: "http://localhost:3000"
    test-command-api: "npm run test:api"
```
