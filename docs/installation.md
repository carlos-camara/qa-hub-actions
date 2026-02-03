# 🏁 Getting Started

Using **QA Hub Actions** in your workflow is simple. All actions are versioned and ready to be consumed directly from your YAML configurations.

## 🛠️ Basic Usage Pattern

All actions follow a standard reference pattern:

```yaml
- uses: carlos-camara/qa-hub-actions/<action-name>@main
  with:
    <input-parameter>: <value>
```

> [!NOTE]
> While `@main` is convenient for the latest features, we recommend pinning to a specific version (e.g., `@v1`) for production stability.

## 🚀 Building your first Pipeline

Here is a recommended baseline for a modern QA pipeline using our core actions:

```yaml
jobs:
  automation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # 1. Setup Python & Node with automatic caching
      - uses: carlos-camara/qa-hub-actions/setup-environment@main
        with:
          node-version: '20'
          python-version: '3.11'

      # 2. Run your specific test suite
      - uses: carlos-camara/qa-hub-actions/run-tests@main
        with:
          run-api: 'true'
          test-command-api: "npm run test:api"

      # 3. Publish results with a PR summary
      - uses: carlos-camara/qa-hub-actions/collect-and-publish@main
        if: always()
        with:
          reports-path: "results"
```

## 🔐 Credentials & Secrets

Most actions use the default `GITHUB_TOKEN` automatically. For integrations like Slack or S3, you will need to provide your own secrets as inputs.

---
*Ready to scale? Explore the specific actions in the sidebar.*
