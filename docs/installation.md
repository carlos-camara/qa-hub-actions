# 🚀 Getting Started

Standardizing your QA pipelines with **QA Hub Actions** is straightforward. Our actions are designed to be modular, reusable, and compatible with any GitHub repository.

## 📦 Installation

Since these are GitHub Actions, there is no "installation" in the traditional sense. You simply reference them in your workflow files.

### Basic Implementation

Add a step to your `.github/workflows/your-pipeline.yml`:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # 1. Setup the environment
      - uses: carlos-camara/qa-hub-actions/setup-environment@main
        with:
          python-version: '3.11'
          node-version: '20'

      # 2. Run your tests
      - uses: carlos-camara/qa-hub-actions/run-tests@main
        with:
          test-command-api: "pytest tests/api"
```

## 🔐 Security & Permissions

Most actions require the standard `${{ secrets.GITHUB_TOKEN }}`. For actions that interact with external services (like Slack or AWS S3), you'll need to configure the appropriate Secrets in your repository settings.

## 🗺️ Pathing Standards

Our actions follow a "standard pathing" convention but are fully configurable. By default, they expect:
- `reports/` for test results.
- `requirements.txt` for Python dependencies.
- `package.json` for Node.js dependencies.

---
[Explore the Action Catalog](index.md#action-ecosystem)
