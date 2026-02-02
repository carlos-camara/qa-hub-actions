# 🧹 Lint Codebase Standard

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**A unified quality gate enforcing standard linting rules across all QA Hub projects.**

</div>

---

## 🚀 Overview

This action strictly enforces code quality standards using GitHub's Super-Linter. It comes pre-configured with the "QA Hub Standard" ruleset, ignoring common noise (build artifacts, reports) and verifying critical languages (Python, YAML, Markdown, TS).

### Key Features
- **🛡️ Zero-Config Defaults**: Works out of the box with optimal settings.
- **⚡ Optimized Exclusion**: Pre-configured to ignore `.venv`, `node_modules`, `reports/`, etc.
- **🔍 Diff-Only Validation**: By default, verifies only *changed* files in Pull Requests for speed.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/lint-codebase@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    validate-all: "false" # Default for PRs
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `github-token` | **REQUIRED**. Token to post status checks. | **Yes** | - |
| `validate-all` | Scan all files (`true`) or only changes (`false`). | No | `false` |
| `default-branch` | Branch to compare against for diffs. | No | `main` |
| `validate-python` | Lint Python files (Black, Flake8). | No | `true` |
| `validate-yaml` | Lint YAML files (yamllint). | No | `true` |
| `validate-markdown` | Lint Markdown files (markdownlint). | No | `true` |
| `validate-ts` | Lint TypeScript/JS/TSX (eslint). | No | `true` |
| `validate-actions` | Lint GitHub Actions workflows. | No | `true` |
| `filter-regex-exclude` | Regex for ignored paths. | No | `(\.venv/\|...` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
