# 📝 Action: PR Hygiene Validator

<div align="center">
  <p><i>Ensure absolute consistency across repository commit history and Pull Request descriptions.</i></p>
</div>

---

> [!IMPORTANT]
> A clean git history is critical for automated release notes and overall repository health. The **PR Hygiene Validator** enforces [Conventional Commits](https://www.conventionalcommits.org/) formatting for Pull Request titles and ensures that all PR bodies meet a minimum character length, preventing empty or unhelpful merge descriptions.

## 🚀 Quick Start

Drop this snippet into your PR intelligence workflow:

```yaml
steps:
  - name: 📝 Validate PR Hygiene
    uses: carlos-camara/qa-hub-actions/pr-hygiene-validator@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      min-description-length: '30' # Optional modifier
```

## ⚙️ Configuration

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `github-token` | Your `GITHUB_TOKEN` for API authentication to add comments if the PR fails hygiene checks. | **Yes** | N/A |
| `min-description-length` | The absolute minimum character count required in the PR body description. | No | `15` |
