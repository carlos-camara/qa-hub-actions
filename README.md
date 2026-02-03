# 🤖 QA Hub Actions

<div align="center">

  <img src="https://socialify.git.ci/carlos-camara/qa-hub-actions/image?description=Enterprise-grade%20reusable%20GitHub%20Actions%20for%20modern%20QA%20pipelines.&font=Inter&language=1&name=QA%20Hub%20Actions&owner=1&pattern=Circuit%20Board&theme=Dark" alt="QA Hub Actions" width="640" height="320" />

  <br />

  [![Wiki](https://img.shields.io/badge/Documentation-Wiki-blue?style=for-the-badge&logo=github&logoColor=white)](https://carlos-camara.github.io/qa-hub-actions/)
  [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
  [![Actions](https://img.shields.io/badge/Actions-13-orange?style=for-the-badge)](https://carlos-camara.github.io/qa-hub-actions/#core-engine)

  <br />
  
  <p>
    <b>Standardizing the standard of quality.</b>
    <br>
    A collection of modular, professional-grade GitHub Actions designed to provide deep visibility and consistent quality across all your repositories.
  </p>

</div>

---

## ⚡ The Pipeline Ecosystem

Our actions are architected to work as a unified ecosystem, moving from environment preparation to stakeholder notification.

```mermaid
graph LR
    A["🚀 Setup Environment"] -- 1. Prepare --> B["🧪 Run QA Test Suite"]
    B -- 2. Execute --> C["📊 Collect & Publish"]
    C -- 3. Report --> D{"Integrations"}
    D -- Notify --> E["📢 Slack Notification"]
    D -- Audit --> F["🛡️ Security Audit"]
    
    style A fill:#e8eaf6,stroke:#3f51b5,stroke-width:2px
    style B fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
    style C fill:#fce4ec,stroke:#e91e63,stroke-width:2px
    style E fill:#fff3e0,stroke:#ff9800,stroke-width:2px
```

## 📦 Action Registry

| Category | Actions |
| :--- | :--- |
| **🚀 Core Engines** | [Run Tests](./run-tests) • [Setup Env](./setup-environment) • [Collect & Publish](./collect-and-publish) |
| **🛡️ Quality & Sec** | [Security Audit](./security-audit) • [Link Checker](./link-checker) • [Linting](./lint-codebase) • [Performance](./performance-baseline-check) |
| **📢 Distribution** | [Slack](./slack-notify) • [GH Pages](./deploy-gh-pages) • [AWS S3](./deploy-reports-s3) |
| **🏗️ Maintenance** | [Labels](./pr-labeler) • [Auto-Release](./python-auto-release) |

## 🚀 Getting Started in 30 Seconds

```yaml
steps:
  - uses: actions/checkout@v4
  
  # 1. Setup multi-runtime env with caching
  - uses: carlos-camara/qa-hub-actions/setup-environment@v1

  # 2. Run your specific engine (API/GUI/Perf)
  - uses: carlos-camara/qa-hub-actions/run-tests@v1
    with:
      test-command-api: "python -m pytest tests/"

  # 3. Aggregate 100% of results & post PR Summary
  - uses: carlos-camara/qa-hub-actions/collect-and-publish@v1
    if: always()
```

## 📖 Deep Documentation

For detailed input/output parameters, advanced configurations, and real-world examples, visit our official documentation site:

🔗 **[https://carlos-camara.github.io/qa-hub-actions/](https://carlos-camara.github.io/qa-hub-actions/)**

---

<p align="center">
  Built with ❤️ for the QA Engineering community.
</p>
