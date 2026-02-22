# 📝 PR Hygiene Validator Action

Validates that incoming Pull Requests adhere to the project standards:
1. **Title Validation:** Ensures the PR title follows the [Conventional Commits](https://www.conventionalcommits.org/) format (e.g., `feat: ...`, `fix: ...`, `chore: ...`).
2. **Description Validation:** Checks that the PR description (body) contains enough meaningful content to aid reviews.

## 🚀 Usage

```yaml
steps:
  - name: Validate PR Hygiene
    uses: carlos-camara/qa-hub-actions/pr-hygiene-validator@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      min-description-length: '15' # Optional
```
