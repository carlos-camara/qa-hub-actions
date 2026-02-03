# 📔 Global Action Wiki

Welcome to the central repository of **QA Hub Actions**. This page provides a high-level technical summary of every tool available in our ecosystem.

---

## 🚀 Core Engine
*The foundation of your CI/CD pipelines.*

### [🧪 Run QA Test Suite](actions/run-tests.md)
The primary execution engine. Supports Pytest, Behave, and Locust.
- **Key Inputs**: `test-command-api`, `test-command-gui`, `headless`, `enable-coverage`.
- **Best Practice**: Use `health-check-urls` to ensure services are ready before testing.

### [⚙️ Setup QA Environment](actions/setup-environment.md)
Standardizes Python and Node.js environments with automated caching.
- **Key Inputs**: `python-version`, `node-version`, `python-install-command`.
- **Why use it?**: Reduces boilerplate and speeds up runs by ~40% via optimized caching.

### [📊 Collect & Publish](actions/collect-and-publish.md)
Aggregates JUnit reports and screenshots into a single PR comment.
- **Key Inputs**: `reports-path`, `screenshots-path`, `publish-results`.
- **Output**: Unified PR status and job summary.

---

## 🛡️ Quality & Security
*Automated guardrails for code and dependencies.*

### [🛡️ Security Audit](actions/security-audit.md)
Scans for CVEs (Safety) and performs static analysis (Bandit).
- **Key Inputs**: `target-path`, `scan-dependencies`.

### [🧶 Lint Codebase](actions/lint-codebase.md)
Standardized linting for Python, YAML, Markdown, and TS.
- **Key Inputs**: `github-token`, `validate-all`.

### [🔗 Link Checker](actions/link-checker.md)
Finds and reports broken links in documentation.
- **Key Inputs**: `search-path`.

### [📉 Performance Baseline](actions/performance-baseline-check.md)
Audits latency regressions against a JSON baseline.
- **Key Inputs**: `current-metrics`, `baseline-metrics`, `threshold`.

---

## 📢 Reporting & Notifications
*Visibility and stakeholder communication.*

### [📢 Slack Notification](actions/slack-notify.md)
Rich, formatted alerts for test success or failure.
- **Key Inputs**: `slack-webhook-url`, `status`, `test-summary`.

### [📂 Deploy Pages](actions/deploy-gh-pages.md)
Direct deployment to GitHub Pages (perfect for this Wiki!).

### [☁️ Deploy S3](actions/deploy-reports-s3.md)
Syncs reports and screenshots to AWS S3.

### [📥 Upload Results](actions/upload-results.md)
Commits test results back to a repository branch.

---

## 🤖 Maintenance & Automation

### [🏷️ PR Labeler](actions/pr-labeler.md)
Automatic triage based on file paths.

### [🚀 Auto-Release](actions/python-auto-release.md)
Semantic versioning and GitHub Releases.

---

> [!NOTE]
> All actions are maintained by the **Advanced Agentic Coding** team. For support or new features, please check the [Contributing](contributing.md) guide.
