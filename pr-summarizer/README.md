# <div align="center">🤖 Action: PR Summarizer</div>

<div align="center">
  <p><i>AI-powered deep technical analysis and high-fidelity visual summaries for Pull Requests, providing surgical visibility into code impact.</i></p>
</div>


---

## 🚀 Key Impact

- **🏗️ Structural Intelligence**: Automatically identifies new classes, functions, and deleted methods with professional badges (`[NEW]`, `[MOD]`, `[FIX]`).
- **🌐 API Footprint**: Scans for new or modified API routes (Express/Flask) and documents the effective impact.
- **🎯 Locator Awareness**: Highlights exactly which UI locators were updated in `.yaml` files for GUI test suites.
- **📊 Impact Analysis**: Generates a dynamic metrics table with visual intensity bars (█) to represent the volume of changes.
- **✨ Gherkin Insights**: Extracts new BDD scenarios and quality tags (`@smoke`, `@critical`) from changed feature files.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | GitHub token for PR description/comment updates. |
| `target` | No | `description` | Where to post the summary: `description` or `comment`. |
| `domain-mapping` | No | `{}` | Optional JSON mapping of file patterns to domains. |

---

## ⚡ Quick Start

```yaml
- name: 🤖 Generate AI Summary
  uses: carlos-camara/qa-hub-actions/pr-summarizer@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    target: "description"
```

---

## 📊 Impact Analysis Example

The action injects a premium overview into your PR:

| Category | Scope | Status |
| :--- | :---: | :--- |
| **Backend** | 5 | █████ |
| **Testing** | 12 | ████████████ |
| **Docs** | 3 | ███ |

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-summarizer/)
</div>
