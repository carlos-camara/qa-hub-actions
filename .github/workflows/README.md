# <div align="center">⚙️ QA Hub Actions: Workflows</div>

<div align="center">
  <p><i>Documentation of the internal continuous integration and continuous delivery (CI/CD) pipelines orchestrating the quality, testing, and deployment of this repository.</i></p>
</div>

---

## 🏗️ Architecture

Because this repository (`qa-hub-actions`) serves as the foundational infrastructure for multiple downstream projects, its own workflows are strictly designed to "drink our own champagne".

We utilize our own generic actions (e.g., `lint-codebase`, `pr-summarizer`) to test and valid the GitHub Actions ecosystem itself.

### Active Workflows

| Workflow | File | Trigger | Purpose |
| :--- | :--- | :--- | :--- |
| **Linting & Code Quality** | `lint.yml` | `pull_request` | Automatically enforce Markdown, YAML, and Python formatting using the `lint-codebase` action. Ensures all code and documentation is pristine. |
| **PR Intelligence** | `pr_intelligence.yml` | `pull_request` | Runs a suite of governance checks: standardizes PR sizes, auto-labels based on file churn (DevOps, Python, Docs), detects Test Debt via `pr-churn-analyzer`, and generates AI summaries via `pr-summarizer`. |

---

## 🛡️ Best Practices

- **Self-Testing:** Any new action added to this repository MUST, whenever possible, include a test execution phase inside one of these workflows to validate its correctness on `main` before consumers adopt it.
- **Strict Governance:** As enforced by `.github/CODEOWNERS`, any PR modifying files within this directory (`.github/workflows/`) requires explicit approval by `@carlos-camara` before merging.
- **Dependency Management:** All workflows and internal dependencies are continuously bumped and audited by Dependabot (configured in `.github/dependabot.yml`).

---

<div align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/carlos-camara/qa-hub-actions/lint.yml?branch=main&logo=github&style=for-the-badge" alt="Lint Status" />
</div>
