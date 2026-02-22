# 🛑 Action: Gate Check (Open PR)

<div align="center">
  <p><i>Intelligently pause or redirect CI/CD execution flows by verifying the existence of active Pull Requests.</i></p>
</div>

---

> [!CAUTION]
> The **Gate Check (Open PR)** action is a flow-control primitive. It prevents redundant pipeline executions if the current working branch already has an active Pull Request open against the mainline branch.

## 🚀 Key Impact

- **🛑 Execution Gating**: Conditionally abort workflows or skip subsequent steps based on PR status.
- **🔄 Conditional Routing**: Allows your pipeline to dynamically change behavior if a PR is detected.
- **⚡ Zero Dependency**: Uses standard GitHub CLI (`gh`) for high performance.

---

## ⚙️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `github-token` | **Yes** | - | Token to authenticate with CLI. |
| `head-branch` | **Yes** | - | Head branch to check for. |
| `base-branch` | No | `main` | Base branch the PR targets. |
| `fail-on-missing` | No | `false` | Fail the step if no PR is found. |

---

## ⚡ Quick Start

```yaml
- name: 🛑 Check if PR is Open
  id: check_pr
  uses: carlos-camara/qa-hub-actions/gate-check-pr@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    head-branch: ${{ github.ref_name }}
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/gate-check-pr/)
</div>
