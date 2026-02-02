# 📢 Slack QA Notification

Send rich, formatted test status notifications directly to your Slack channels. Keep your team informed about build health with zero effort.

## 🛠 Features

- **Status-Aware Coloring**: Green for success, red for failures, grey for cancellations.
- **Deep Links**: Automatically includes links to the specific GitHub Action run for easy debugging.
- **Custom Summaries**: Support for dynamic markdown summaries from your test cycles.

## 📥 Inputs

| Name | Description | Default |
| :--- | :--- | :--- |
| `slack-webhook-url` | **Required**. Your Slack Incoming Webhook URL. | - |
| `status` | Current run status (`success`, `failure`). | `success` |
| `test-summary` | Text summary of the results. | `Tests completed successfully.` |
| `project-name` | Name of the project. | `${{ github.repository }}` |

## 🚀 Usage

```yaml
- uses: qa-hub-actions/slack-notify@v1
  if: always()
  with:
    slack-webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    status: ${{ job.status }}
    test-summary: |
      *API Tests*: 45 Passed, 2 Failed
      *GUI Tests*: 10 Passed, 0 Failed
```

> [!TIP]
> Use this action in conjunction with `collect-and-publish` to send the most up-to-date summaries to your team.
