# 🤖 QA Hub Actions

<div align="center">

  <img src="https://socialify.git.ci/carlos-camara/qa-hub-actions/image?description=Enterprise-grade%20reusable%20GitHub%20Actions%20for%20modern%20QA%20pipelines.&font=Inter&language=1&name=QA%20Hub%20Actions&owner=1&pattern=Circuit%20Board&theme=Dark" alt="QA Hub Actions" width="640" height="320" />

  <br />

  <a href="https://carlos-camara.github.io/qa-hub-actions/"><img src="https://img.shields.io/badge/Documentation-Wiki-blue?style=for-the-badge&logo=github&logoColor=white" alt="Wiki" /></a>
  <a href="https://github.com/carlos-camara/qa-hub-actions/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" /></a>
  <a href="https://github.com/carlos-camara/qa-hub-actions/"><img src="https://img.shields.io/badge/Actions-19-orange?style=for-the-badge" alt="Actions" /></a>

  <br />
  
  <p>
    <b>The Industry Standard for Quality Orchestration.</b>
  </p>
  
> [!IMPORTANT]
> A suite of 19+ surgical, modular, and enterprise-grade GitHub Actions architected to provide maximum technical visibility, aesthetic summaries, and absolute consistency across the engineering lifecycle.

</div>

---

## 🏗️ Technical Orchestration

Our ecosystem moves seamlessly from infrastructure readiness to executive intelligence.

```mermaid
graph LR
    subgraph "Phase 1: Readiness"
        A["🚀 Setup Env"] --> B["🏥 Health Check"]
    end
    
    subgraph "Phase 2: Execution"
        B --> C["🧪 Run Tests"]
        C --> D["📊 Collect"]
    end
    
    subgraph "Phase 3: Intelligence"
        D --> E["🤖 Summarize"]
        E --> F["📢 Notify"]
    end
    
    style A fill:#0f172a,color:#fff,stroke:#38bdf8
    style B fill:#0f172a,color:#fff,stroke:#38bdf8
    style C fill:#0f172a,color:#fff,stroke:#38bdf8
    style D fill:#0f172a,color:#fff,stroke:#38bdf8
    style E fill:#0f172a,color:#fff,stroke:#c084fc
    style F fill:#0f172a,color:#fff,stroke:#c084fc
```

---

## 🏪 Action Marketplace

Explore our curated collection of professional CI/CD utilities.

### 🏎️ Core Performance & Execution
| Action | Description | Status |
| :--- | :--- | :--- |
| [**🧪 Run Tests**](actions/run-tests.md) | Multi-engine execution (API/GUI/Perf) with automated retry logic and timestamped isolation. | `Stable` |
| [**🐍 Setup Env**](actions/setup-environment.md) | High-speed multi-runtime (Python/Node) setup with intelligent dependency caching. | `Stable` |
| [**📊 Collect & Publish**](actions/collect-and-publish.md) | Merges multi-project results into a single, high-fidelity visual summary. | `Updated` |
| [**🏥 Env Health**](actions/environment-health-check.md) | Validates infrastructure readiness and connectivity before test execution. | `Stable` |

### 🛡️ Quality & Security Guardrails
| Action | Description | Status |
| :--- | :--- | :--- |
| [**🤖 PR Summarizer**](actions/pr-summarizer.md) | AI-powered PR analysis, risk assessment, and code intelligence at a glance. | `Hot` |
| [**🛡️ Security Audit**](actions/security-audit.md) | Surgical detection of leaked secrets and npm/pip vulnerabilities (Safety/Bandit). | `Stable` |
| [**🧶 Lint Codebase**](actions/lint-codebase.md) | Multi-standard enforcement for consistent style (YAML, MD, JS, PY). | `Stable` |
| [**📉 Perf Baseline**](actions/performance-baseline-check.md) | Automated regression check against historical Locust latency baselines. | `Stable` |
| [**🔗 Link Checker**](actions/link-checker.md) | Absolute validation of all internal/external documentation links. | `Stable` |

### 📢 Insights & Distribution
| Action | Description | Status |
| :--- | :--- | :--- |
| [**📢 Slack Notify**](actions/slack-notify.md) | High-fidelity notifications with executive summaries, status badges, and deep links. | `Stable` |
| [**📥 Upload Results**](actions/upload-results.md) | Secure archival of test artifacts and HTML reports to your repository. | `Stable` |
| [**☁️ Deploy S3**](actions/deploy-reports-s3.md) | Cloud-native distribution of QA dashboards to AWS S3 buckets. | `Stable` |
| [**📂 Deploy Pages**](actions/deploy-gh-pages.md) | Automated documentation deployments for internal wikis and dashboards. | `Stable` |

### 🤖 Workflow Intelligence
| Action | Description | Status |
| :--- | :--- | :--- |
| [**🎯 PR Milestoner**](actions/pr-milestoner.md) | Automatic assignment of the latest open milestones to incoming PRs. | `New` |
| [**🏷️ PR Labeler**](actions/pr-labeler.md) | Surgical path-based labeling for complex, multi-layer repositories. | `Stable` |
| [**📏 PR Size**](actions/pr-size-labeler.md) | Automatically estimates PR size (added + deleted lines) and applies standard S/M/L labels. | `Stable` |
| [**📝 PR Hygiene**](actions/pr-hygiene-validator.md) | Validates Conventional Commits and PR description completeness. | `Stable` |
| [**🤖 PR Risk**](actions/pr-risk-analyzer.md) | Scans for modifications in critical system files and marks high-risk PRs with visual alerts. | `Stable` |
| [**📝 Release Notes**](actions/qa-release-notes.md) | Automated generation of quality-focused release dossiers and changelogs. | `Stable` |
| [**📸 Visual Mgr**](actions/visual-regression-manager.md) | Advanced visual regression baseline and delta management utilities. | `Stable` |
| [**🔗 Jira Auto-Tagger**](actions/jira-auto-tagger.md) | End-to-end BDD traceability (Test Plan > Feature > Scenario) with automated status rollups. | `Hot` |

---

## 🚀 Getting Started in 30 Seconds

```yaml
steps:
  - uses: actions/checkout@v6
  
  # 1. Setup multi-runtime env with surgical caching
  - uses: carlos-camara/qa-hub-actions/setup-environment@v1
    with:
      python-version: "3.11"
      node-version: "20"

  # 2. Run your specific engine (API/GUI/Perf)
  - uses: carlos-camara/qa-hub-actions/run-tests@v1
    with:
      test-command-api: "pytest tests/api"

  # 3. Aggregate 100% of results & post Visual Summary
  - uses: carlos-camara/qa-hub-actions/collect-and-publish@v1
    if: always()
```

## 📖 Deep Documentation

> [!NOTE]
> For detailed technical specifications, input/output schemas, and advanced configuration patterns, visit our **Official Wiki**:

🔗 **[https://carlos-camara.github.io/qa-hub-actions/](https://carlos-camara.github.io/qa-hub-actions/)**

---

<div align="center">
  <i>Designed & Engineered by <b><a href="https://github.com/carlos-camara">Carlos Cámara</a></b></i>
</div>
