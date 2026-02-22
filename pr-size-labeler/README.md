# 📏 PR Size Labeler Action

Automatically categorizes Pull Requests by calculating their size (added + deleted lines of code) and applies a descriptive visual label.

Labels applied:
* `size/S`: < 50 lines changed
* `size/M`: 50 - 200 lines changed
* `size/L`: 200 - 500 lines changed
* `size/XL`: > 500 lines changed

*The action is intelligent enough to create the labels in the repository if they don't exist, and to remove old size labels if the PR gets smaller or larger through subsequent commits.*

## 🚀 Usage

```yaml
steps:
  - name: 📥 Checkout Repository
    uses: actions/checkout@v6
    with:
      fetch-depth: 0 # Required to compare against the base branch
      
  - name: 📏 Label PR by Size
    uses: carlos-camara/qa-hub-actions/pr-size-labeler@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
```
