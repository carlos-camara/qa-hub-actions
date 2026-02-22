# 🧶 Action: Lint Codebase

<div align="center">
  <p><i>Enforce consistent code quality standards across Python, YAML, Markdown, and TypeScript with surgical precision.</i></p>
</div>

---

> [!CAUTION]
> The **Lint Codebase** action serves as the absolute gatekeeper for code consistency. It leverages GitHub's `super-linter` to evaluate syntax deviations and block PRs that do not meet professional enterprise standards, ensuring the master branch is always pristine.

## 🚀 Key Impact

- **🔄 Multi-Standard Enforcement**: Validates formatting and syntax for YAML, Markdown, Python, and JavaScript/TypeScript in a single pass.
- **🛡️ Quality Guardrails**: Automatically blocks merges if the codebase deviates from the official QA Hub professional standards.
- **⚡ Partial Validation**: Configurable to only lint modified files, significantly reducing feedback loops in large PRs.
- **📝 Automatic PR Updates**: Optionally updates the PR description checklist when linting passes (via `gh pr edit`).

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | GitHub Token for status checks and PR updates. |
| `default-branch` | No | `main` | Branch used as comparison baseline for changes. |
| `validate-all` | No | `false` | If `true`, scans the entire repository every time. |
| `validate-python` | No | `true` | Toggle Python linting (Black/Flake8). |
| `filter-regex-exclude`| No | `(\.venv/\|...)` | Regex to ignore specific paths or vendor folders. |

---

## ⚡ Quick Start

Drop this snippet into your workflow:

```yaml
steps:
  - name: 🧶 Lint Codebase
    uses: carlos-camara/qa-hub-actions/lint-codebase@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      validate-all: "false"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/lint-codebase/)
</div>
