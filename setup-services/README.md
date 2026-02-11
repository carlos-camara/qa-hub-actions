# 🚀 Setup Services Action

This action orchestrates background services and waits for health check endpoints before test execution. It is designed to be used in conjunction with `run-tests` for a more modular CI/CD pipeline.

## 🏗️ Usage

```yaml
- name: Setup Services
  uses: carlos-camara/qa-hub-actions/setup-services@main
  with:
    start-services-command: "npm run start-backend > backend.log 2>&1 & npm run dev > frontend.log 2>&1 &"
    health-check-urls: "http://localhost:3000 http://localhost:3001/api/health"
    health-check-timeout: '60000'
```

## 🛠️ Inputs

| Input | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `start-services-command` | `String` | **Required** | Command to start background services (e.g., `npm start &`). |
| `health-check-urls` | `String` | **Required** | Space-separated URLs to wait for (e.g., `http://localhost:3000`). |
| `health-check-timeout` | `String` | `60000` | Timeout in milliseconds for health checks. |

## 🆘 Troubleshooting

If the health check fails, the action will attempt to print `backend.log` and `frontend.log` if they exist in the workspace to help debug startup issues.
