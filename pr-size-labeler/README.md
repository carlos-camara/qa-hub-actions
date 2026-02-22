# 📏 Action: PR Size Labeler

<div align="center">
  <p><i>Automatically classify Pull Request scope to optimize Code Review allocation and identify bloated monolithic changes.</i></p>
</div>

---

> [!IMPORTANT]
> The **PR Size Labeler** dynamically evaluates the total delta (added + deleted lines of code) of a Pull Request and applies a standardized size label (`S`, `M`, `L`, `XL`). The engine is self-healing, automatically removing outdated labels if a PR size shrinks or grows through force-pushes or commit squashing.

## 🚀 Quick Start

Drop this snippet into your PR intelligence workflow:

```yaml
steps:
  - name: 📥 Checkout Repository
    uses: actions/checkout@v6
    with:
      fetch-depth: 0 # Required for delta comparison
      
  - name: 📏 Label PR by Size
    uses: carlos-camara/qa-hub-actions/pr-size-labeler@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
```

## ⚙️ Configuration

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `github-token` | Your `GITHUB_TOKEN` for API authentication to add/remove labels in the PR. | **Yes** | N/A |

## 🧬 Sizing Matrix

| Label | Threshold (Lines Changed) | Triage Recommendation |
| :--- | :--- | :--- |
| `size/S` | < 50 lines | Trivial review; fast-track approval acceptable. |
| `size/M` | 50 - 200 lines | Standard review; assign one core reviewer. |
| `size/L` | 200 - 500 lines | Substantial change; requires deep architectural review. |
| `size/XL` | > 500 lines | High overhead; consider rejecting and splitting into multiple PRs. |
