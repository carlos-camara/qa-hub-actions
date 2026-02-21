# <div align="center">🎯 Action: PR Milestoner</div>

<div align="center">
  <p><i>Surgically assign the latest open milestones to your Pull Requests to ensure automated project tracking and roadmap alignment.</i></p>
</div>


---

## 🚀 Key Impact

- **🎯 Automated Alignment**: Automatically detects the most relevant open milestone for any incoming Pull Request.
- **⚖️ Selection Strategies**: Toggle between `latest_created` (default) or `next_due` to match your roadmap methodology.
- **✨ Zero Config**: Integrates seamlessly with standard GitHub Milestones without requiring extra data files.
- **🤖 Triage Efficiency**: Reduces manual maintenance for project managers and developers.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | Token for API access (requires PR editing scope). |
| `strategy` | No | `latest_created` | Selection logic: `latest_created` or `next_due`. |

---

## ⚡ Quick Start

```yaml
- name: 🎯 Assign Milestone
  uses: carlos-camara/qa-hub-actions/pr-milestoner@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    strategy: "next_due"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-milestoner/)
</div>
