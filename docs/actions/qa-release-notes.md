# 📝 Action: QA Release Notes

<div align="center">
  <p><i>Bridge the gap between technical automation and stakeholder visibility by generating high-fidelity, human-readable testing dossiers from your BDD feature files.</i></p>
</div>

---

> [!NOTE]
> The **QA Release Notes** action automatically compiles an executive-level list of newly implemented testing scenarios and behaviors. Perfect for sprint retrospectives and non-technical stakeholders who need visibility into automation expansion.

## 🚀 Key Impact

- **📖 Gherkin Intelligence**: Surgically parses `.feature` files to extract professional titles and scenario checklists.
- **📊 Executive Dossiers**: Generates a structured overview of the testing scope directly in your Job Summary.
- **💬 Stakeholder Alignment**: Optionally posts the testing scope as a PR comment to inform Devs and PMs before merge.
- **🚀 Agile Transparency**: Ensures consistent visibility into automated coverage across every deployment.

---

## 🏗️ Technical Lifecycle

```mermaid
graph TD
    A[Action Start] --> B[Scan .feature files]
    B --> C[Extract Feature Titles]
    C --> D[Extract Scenario Lists]
    D --> E[Format Markdown Summary]
    E --> F[Publish to GH Summary]
    E -- Optional --> G[Post PR Comment]
```

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `features-path` | No | `features` | Root directory to scan for `.feature` files. |
| `github-token` | No | - | Token required for PR commenting. |
| `publish-pr-comment`| No | `false` | Whether to post the summary as a PR comment. |

---

## ⚡ Quick Start

Drop this snippet into your PR workflows:

```yaml
steps:
  - name: 📝 Generate QA Release Notes
    uses: carlos-camara/qa-hub-actions/qa-release-notes@main
    with:
      features-path: "features"
      publish-pr-comment: "true"
      github-token: ${{ secrets.GITHUB_TOKEN }}
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/qa-release-notes/)
</div>
