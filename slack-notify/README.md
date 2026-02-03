# 📢 Slack QA Notification

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Send beautifully formatted test summaries and environment status to a Slack channel.

## ⚡ Quick Info

- **Category**: Reporting & Notifications
- **Complexity**: Low
- **Version**: v1.0.2
- **Required Secrets**: `SLACK_WEBHOOK_URL`

## 🚀 Usage

```yaml
- name: Notify Slack
  uses: carlos-camara/qa-hub-actions/slack-notify@main
  if: always()
  with:
    slack-webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    status: ${{ job.status }}
    test-summary: "Finished execution for PR #${{ github.event.number }}"
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `slack-webhook-url` | The Slack Webhook URL. | `REQUIRED` |
| `status` | Job status (`success`, `failure`, `cancelled`). | `'success'` |
| `test-summary` | Summary text for the notification. | `'Tests completed successfully.'` |
| `project-name` | Name of the project. | `${{ github.repository }}` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/slack-notify/)
