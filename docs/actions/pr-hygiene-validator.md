# 📝 Action: PR Hygiene Validator

<div align="center">
  <p><i>Ensure absolute consistency across repository commit history and Pull Request descriptions.</i></p>
</div>

---

> [!IMPORTANT]
> A clean git history is critical for automated release notes and overall repository health. The **PR Hygiene Validator** enforces [Conventional Commits](https://www.conventionalcommits.org/) formatting for Pull Request titles and ensures that all PR bodies meet a minimum character length.

## 🚀 Key Impact

- **🚥 History Integrity**: Guaranteed Conventional Commits for better automated changelogs.
- **💬 Quality Descriptions**: Prevents empty PR bodies by enforcing minimum length thresholds.
- **🤖 Automated Policing**: Posts corrective feedback directly to the PR for engineer self-service.

---

## ⚙️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | Token for API interactions and comments. |
| `min-description-length` | No | `15` | Minimum character count for the PR body. |

---

## ⚡ Quick Start

```yaml
- name: 📝 Validate PR Hygiene
  uses: carlos-camara/qa-hub-actions/pr-hygiene-validator@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    min-description-length: '30'
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-hygiene-validator/)
</div>
