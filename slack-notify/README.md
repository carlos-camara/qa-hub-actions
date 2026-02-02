# 📢 Slack QA Notification

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Beta-yellow?style=for-the-badge&logo=none)

**Send beautifully formatted, rich test summaries to your Slack channels.**

</div>

---

## 🚀 Overview

Keep your team in the loop with real-time test status updates. This action sends a visually structured Slack message containing the run status, a summary of results, and direct links to the GitHub Actions execution.

### Key Features
- **🎨 Rich Formatting**: Uses Slack attachments with color-coded status (✅ Success / ❌ Failure).
- **🔗 Contextual Links**: Links directly to the specific GitHub Run for quick debugging.
- **📝 Custom Summaries**: Supports passing a custom text summary of the results.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/slack-notify@v1
  if: always()
  with:
    slack-webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
    status: ${{ job.status }}
    test-summary: 'API: 50 passed, 2 failed'
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `slack-webhook-url` | **REQUIRED**. Slack Webhook URL. | **Yes** | - |
| `status` | **REQUIRED**. Run status (`success`, `failure`, `cancelled`). | **Yes** | `success` |
| `test-summary` | Text summary of results. | No | `Tests completed.` |
| `project-name` | Project name for the header. | No | Repo Name |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
