# 📢 Slack Notification

Bring real-time visibility to your test runs with rich, formatted Slack alerts.

## 📖 Overview

This action sends a detailed summary of your test run results (pass/fail status, duration, and meta-data) directly to a Slack channel using Incoming Webhooks.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `slack-webhook-url` | The Slack Webhook URL. | `""` |
| `status` | The result of the test run. | `'success'` |
| `channel` | Optional channel override. | `""` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/slack-notify@main
  if: always()
  with:
    slack-webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    status: ${{ job.status }}
```

---
*Stay informed, react faster.*
