# <div align="center">📝 Changelog</div>

<div align="center">
  <p><i>All notable changes to the QA Hub Actions project will be documented in this file.</i></p>
</div>

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **`CODE_OF_CONDUCT.md`**, **`SECURITY.md`**, and **`CHANGELOG.md`** added to establish project governance and health.
- **`.github/workflows/README.md`** added to document the CI/CD orchestrated pipelines of the registry itself.
- **`dependabot.yml`** created to automatically manage dependencies for `github-actions`, `npm`, and `pip`.
- **`PULL_REQUEST_TEMPLATE.md`** and **`CODEOWNERS`** migrated to standardize contributing.

### Changed
- **`jira-auto-tagger`**: Upgraded to support injecting Atlassian Document Format (ADF) Markdown history tables without overwriting the description.
- **Docs**: Applied premium Glassmorphism-style centered headers to all 18 generic Markdown README files.
- **`pr_intelligence.yml`**: Migrated from Dashboard, customized to analyze generic action structures (`action.yml`, `package.json`), and integrated the `pr-churn-analyzer` action.
- **Auto-Labeler**: Refactored `.github/labeler.yml` to support the monorepo architecture ("Actions: Definition", "Logic: Python").

---

## [1.2.0] - 2026-02-14

### Added
- **`jira-reporter.py`**: Integration with Jira API v3 for dynamic test execution history and status state synchronization.
- **Action Marketplace**: Refined the main `README.md` to highlight high-value actions like the `jira-auto-tagger`.
