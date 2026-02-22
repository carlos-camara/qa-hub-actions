# 🧠 Action: PR Intelligence

<div align="center">
  <p><i>The advanced cognitive engine for automated Pull Request orchestration and risk governance.</i></p>
</div>

---

> [!IMPORTANT]
> The **PR Intelligence** engine is the flagship of the QA Hub ecosystem. It provides a multi-vector analysis of Pull Requests, combining hygiene validation, size labeling, and critical file risk detection into a single, high-performance execution.

## 🚀 Key Impact

- **🧠 Cognitive Orchestration**: Simultaneously handles PR hygiene, labeling, and risk analysis.
- **🛡️ Governance Guardrails**: Automatically flags high-risk changes to mission-critical files.
- **📏 Automated Sizing**: Dynamically labels PRs by complexity to optimize reviewer focus.
- **🚥 Standardized Quality**: Enforces Conventional Commits across the entire engineering team.

---

## ⚙️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | Token with PR and labels write permissions. |
| `critical-patterns` | No | `environment.py,config.yaml,...` | Patterns to trigger risk alerts. |
| `validate-hygiene` | No | `true` | Enable Conventional Commit validation. |
| `label-size` | No | `true` | Enable automated XL/L/M/S labeling. |
| `analyze-risk` | No | `true` | Enable detection of critical file changes. |

---

## ⚡ Quick Start

```yaml
- name: 🧠 Run Intelligence Engine
  uses: carlos-camara/qa-hub-actions/pr-intelligence@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-intelligence/)
</div>
