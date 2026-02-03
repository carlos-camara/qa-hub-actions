# 🧶 Lint Codebase

!!! info "At a Glance"
    - **Category**: Quality & Security
    - **Complexity**: Low
    - **Version**: v1.5.0 (Stable)
    - **Primary Tool**: Super-Linter / Flake8

Unified linting engine to ensure code style consistency across the entire repository.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `github-token` | GitHub Token for posting status checks. | `REQUIRED` |
| `default-branch` | Default branch for comparison (e.g. `main`). | `'main'` |
| `validate-all` | Validate entire codebase (`true`) or just changes (`false`). | `'false'` |
| `validate-python` | Lint Python files? | `'true'` |
| `validate-yaml` | Lint YAML files? | `'true'` |
| `validate-markdown` | Lint Markdown files? | `'true'` |
| `validate-actions` | Lint GitHub Actions? | `'true'` |
| `validate-ts` | Lint TypeScript/JS? | `'true'` |
| `filter-regex-exclude` | Regex for ignored paths. | `(\.venv/|_pycache_/|reports/|\.git/|\.pytest_cache/|node_modules/|dist/|coverage/)` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/lint-codebase@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    validate-all: 'true'
```

---
*Clean code, consistent results.*
