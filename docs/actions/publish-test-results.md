# 📢 Action: Publish Test Results

<div align="center">
  <p><i>Parse JUnit XML results and post professional, high-fidelity summaries directly into your Pull Request description or comments for immediate team visibility.</i></p>
</div>

---

> [!IMPORTANT]
> The **Publish Test Results** action transforms raw execution data into aesthetic, human-readable intelligence. By injecting success rates, durations, and failure traces directly into GitHub, it eliminates the need for developers to dig through raw console logs.

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

Drop this snippet into your workflow:

```yaml
steps:
  - name: 📢 Publish Test Results
    uses: carlos-camara/qa-hub-actions/publish-test-results@main
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
