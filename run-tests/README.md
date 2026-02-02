# 🧪 Run QA Test Suite

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**The core execution engine for running API, GUI, and Performance tests in parallel.**

</div>

---

## 🚀 Overview

This action is the workhorse of the QA Hub pipeline. It handles the complexity of starting background services, checking their health, and then orchestrating the parallel or sequential execution of multiple test types (API, GUI, Performance).

### Key Features
- **🚦 Service Orchestration**: Starts your app (e.g., `npm start`) and waits until it's ready.
- **⚡ Parallel Execution**: Can run multiple test suites within the same job context.
- **🖥️ Headless Support**: Configures environment for headless browser testing automatically.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/run-tests@v1
  with:
    start-services-command: 'npm start &'
    health-check-urls: 'http://localhost:3000'
    test-command-api: 'npm run test:api'
    test-command-gui: 'npm run test:gui'
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `start-services-command` | Command to start background services. | No | `''` |
| `health-check-urls` | URLs to wait for using `wait-on`. | No | `''` |
| `test-command-api` | Command to run API tests. | No | `''` |
| `test-command-gui` | Command to run GUI tests. | No | `''` |
| `test-command-performance` | Command to run Performance tests. | No | `''` |
| `run-api` | Toggle API tests execution. | No | `true` |
| `run-gui` | Toggle GUI tests execution. | No | `true` |
| `run-performance` | Toggle Performance tests execution. | No | `true` |
| `headless` | Run GUI tests in headless mode. | No | `true` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
