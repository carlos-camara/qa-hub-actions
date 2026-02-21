# <div align="center">📢 Action: Slack Notification</div>

<div align="center">
  <p><i>Send beautifully formatted test summaries, environment status, and high-fidelity alerts to your team's Slack channels.</i></p>
</div>


---

## 🚀 Key Impact

- **🎨 High-Fidelity Layouts**: Delivers rich Slack attachments with status-colored sidebars (Success: Green, Failure: Red).
- **📊 Run Intelligence**: Automatically includes deep links to the specific GitHub Action run for surgical debugging.
- **🛠️ Configurable Summaries**: Injects custom test metrics or context-specific summaries into every notification.
- **🦾 Automation Focused**: Designed to run in the `always()` hook to ensure visibility regardless of job outcome.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `slack-webhook-url` | **Yes** | - | Your incoming Slack Webhook URL. |
| `status` | **Yes** | `success` | Job status: `success`, `failure`, or `cancelled`. |
| `test-summary` | No | (Table) | Brief text describing the execution results. |
| `project-name` | No | (Repo) | Identifier for the project being tested. |

---

## ⚡ Quick Start

```yaml
- name: 📢 Notify Slack
  uses: carlos-camara/qa-hub-actions/slack-notify@main
  if: always()
  with:
    slack-webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    status: ${{ job.status }}
    test-summary: "Test Suite Results: 45 Passed, 2 Failed."
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/slack-notify/)
</div>
