# 🧶 Lint Codebase

!!! info "At a Glance"
    - **Category**: Quality & Security
    - **Complexity**: Low
    - **Version**: v1.5.0 (Stable)
    - **Primary Tool**: Super-Linter / Flake8

Unified linting engine to ensure code style consistency across the entire repository.

## 📖 Overview

Uses standardized linting rules to analyze your code. It supports multiple languages via the internal Super-Linter configuration, ensuring every PR follows your team's style guide.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `github-token` | Token for posting status checks. | `${{ github.token }}` |
| `validate-python` | Whether to lint Python files. | `'true'` |
| `validate-javascript` | Whether to lint JavaScript files. | `'true'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/lint-codebase@main
```

---
*Clean code, consistent results.*
