# 📢 Action: Publish Test Results

Parse JUnit XML results and post professional, high-fidelity summaries directly into your Pull Request description or comments for immediate team visibility.

---

## 🚀 Key Impact

- **📊 Aesthetic Summaries**: Converts technical JUnit XML files into clean, human-readable Markdown tables.
- **💬 PR Integration**: Intelligently injects results into your PR description or posts updatable comments.
- **🔄 Step Summary**: Automatically appends the test suite results to the GitHub Actions Job Summary.
- **🛠️ Flexible Targeting**: Choose exactly where you want the feedback to appear: `description` or `comment`.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `reports-path` | **Yes** | - | Path to the directory containing JUnit XML reports. |
| `github-token` | **Yes** | - | GitHub Token for API interactions. |
| `title` | No | `Test Execution Summary` | Custom title for the published report. |
| `target` | No | `description` | Where to publish: `description` or `comment`. |

---

## ⚡ Quick Start

```yaml
- name: 📢 Publish Test Results
  uses: carlos-camara/qa-hub-actions/publish-test-results@v1
  if: always()
  with:
    reports-path: "junit-results/"
    github-token: ${{ secrets.GITHUB_TOKEN }}
    target: "comment"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/publish-test-results/)
</div>
