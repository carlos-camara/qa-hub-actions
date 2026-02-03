# 🧶 Lint Codebase Standard

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Runs Super-Linter with standardized rules for QA Hub projects.

## ⚡ Quick Info

- **Category**: Quality & Security
- **Complexity**: Low
- **Version**: v1.5.0

## 🚀 Usage

```yaml
- name: Lint Codebase
  uses: carlos-camara/qa-hub-actions/lint-codebase@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    validate-all: 'false'
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `github-token` | GitHub Token for status checks. | `REQUIRED` |
| `default-branch` | Branch for comparison. | `'main'` |
| `validate-all` | Validate entire codebase? | `'false'` |
| `filter-regex-exclude` | Regex for ignored paths. | `(\.venv/...` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/lint-codebase/)
