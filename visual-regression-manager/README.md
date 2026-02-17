# 📸 Action: Visual Regression Mgr

Automate the lifecycle of your visual baselines by promoting latest screenshots to gold-standards upon manual approval or specific triggers.

---

## 🚀 Key Impact

- **🎯 Precision Promotion**: Automatically maps `*_latest.png` artifacts to their corresponding gold-standard baseline paths.
- **🤖 Driver Awareness**: Handles driver-specific prefixes (e.g., `chrome_`, `playwright_`) to ensure multi-browser consistency.
- **🚀 Automated Deployment**: Commits and pushes the promoted baselines directly to your branch with surgical precision.
- **⚙️ Artifact Intelligence**: Intelligent handling of multi-browser visual regressions in a single, unified interface.

---

## 🏗️ Technical Workflow

1. **Input**: Receive the Run ID of a failed test run containing approved visual changes.
2. **Download**: Automatically fetch the `gui-screenshots` artifact from the specified run.
3. **Map & Promote**: Safely overwrite existing baselines with the new approved images.
4. **Deploy**: Push changes back to the repository using professional bot identities.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `run-id` | **Yes** | - | ID of the workflow run to fetch screenshots from. |
| `github-token` | **Yes** | - | GitHub token with write permissions. |
| `driver-type` | No | `chrome` | Driver prefix used in baseline naming. |
| `baseline-path` | No | (Table) | Local path where baselines are stored. |
| `screenshots-artifact` | No | `gui-screenshots` | Name of the artifact containing new visuals. |

---

## ⚡ Quick Start

```yaml
- name: 📸 Promote approved baselines
  uses: carlos-camara/qa-hub-actions/visual-regression-manager@main
  with:
    run-id: ${{ github.event.inputs.run_id }}
    github-token: ${{ secrets.GITHUB_TOKEN }}
    driver-type: "playwright"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/visual-regression-manager/)
</div>
