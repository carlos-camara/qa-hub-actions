# 📢 Slack Notification

!!! info "At a Glance"
    - **Category**: Reporting & Notifications
    - **Complexity**: Low
    - **Version**: v1.0.2 (Beta)
    - **Primary Tool**: Incoming Webhooks

Bring real-time visibility to your test runs with rich, formatted Slack alerts.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `slack-webhook-url` | The Slack Webhook URL to send the notification to. | `REQUIRED` |
| `status` | The status of the test run (e.g., `success`, `failure`, `cancelled`). | `'success'` |
| `test-summary` | A brief summary of the test results to include in the message. | `'Tests completed successfully.'` |
| `project-name` | The name of the project being tested. | `${{ github.repository }}` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/slack-notify@main
  if: always()
  with:
    slack-webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    status: ${{ job.status }}
    test-summary: "Finished execution for PR #${{ github.event.number }}"
```

---
*Stay informed, react faster.*
