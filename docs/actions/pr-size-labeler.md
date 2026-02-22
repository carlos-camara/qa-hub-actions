# 📏 Action: PR Size Labeler

<div align="center">
  <p><i>Automatically classify Pull Request scope to optimize Code Review allocation and identify bloated monolithic changes.</i></p>
</div>

---

> [!IMPORTANT]
> The **PR Size Labeler** dynamically evaluates the total delta of a Pull Request and applies a standardized size label (`S`, `M`, `L`, `XL`). The engine is self-healing, automatically removing outdated labels if a PR size shrinks.

## 🚀 Key Impact

- **📏 Automated Sizing**: Provides instant visibility into the "cost" of a PR.
- **🚥 Review Optimization**: Helps teams prioritize smaller, safer changes in the queue.
- **🔄 State Consistency**: Automatically adjusts labels as new commits are pushed to the PR.

---

## ⚙️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | Token for adding/removing labels. |

---

## ⚡ Quick Start

```yaml
- name: 📏 Label PR by Size
  uses: carlos-camara/qa-hub-actions/pr-size-labeler@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-size-labeler/)
</div>
