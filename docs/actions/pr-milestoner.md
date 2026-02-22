# 🎯 Action: PR Milestoner

<div align="center">
  <p><i>Surgically assign the latest open milestones to your Pull Requests to ensure automated project tracking and roadmap alignment.</i></p>
</div>

---

> [!IMPORTANT]
> The **PR Milestoner** automatically detects and aligns incoming Pull Requests with your project's active milestones. This eliminates manual tracking overhead and ensures that your release notes and agile boards are always synchronized with actual code velocity.

## 🚀 Quick Start

Drop this snippet into your PR intelligence workflow:

```yaml
steps:
  - name: 🎯 Assign Milestone
    uses: carlos-camara/qa-hub-actions/pr-milestoner@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      strategy: "next_due"
```

## ⚙️ Configuration

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `github-token` | Token for API access (requires PR editing scope). | **Yes** | N/A |
| `strategy` | Selection logic: `latest_created` or `next_due`. | No | `latest_created` |

---



---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-milestoner/)
</div>
