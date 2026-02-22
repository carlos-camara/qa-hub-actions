# 🚀 Action: Setup Services

<div align="center">
  <p><i>Orchestrate background services and perform automated health checks to ensure infrastructure readiness before any test execution.</i></p>
</div>

---

> [!IMPORTANT]
> The **Setup Services** action eliminates race conditions in your CI/CD by intelligently standing up backend and frontend architectures, guaranteeing that the target endpoints are fully healthy (`HTTP 200`) before yielding control back to the runner.

## 🚀 Key Impact

- **🏗️ Service Orchestration**: Seamlessly launches backend and frontend processes in the background for integrated testing.
- **🩺 Automated Health Checks**: Waits for specific endpoints to return `200 OK` before allowing the pipeline to proceed.
- **🔍 Debug Intelligence**: Automatically captures and prints service logs (`backend.log`, `frontend.log`) upon startup failure.
- **⚡ Performance-Focused**: Minimizes waiting time with configurable timeouts and intelligent retry logic.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `start-services-command` | **Yes** | - | Shell command to start background services. |
| `health-check-urls` | **Yes** | - | Space-separated URLs to wait for (health endpoints). |
| `health-check-timeout` | No | `60000` | Maximum time to wait for services in milliseconds. |

---

## ⚡ Quick Start

Drop this snippet into your workflow:

```yaml
steps:
  - name: 🚀 Setup Application Services
    uses: carlos-camara/qa-hub-actions/setup-services@main
    with:
      start-services-command: "npm start &"
      health-check-urls: "http://localhost:3000/health"
      health-check-timeout: "45000"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/setup-services/)
</div>
