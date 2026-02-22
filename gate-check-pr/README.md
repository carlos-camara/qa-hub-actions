# 🛑 Action: Gate Check (Open PR)

<div align="center">
  <p><i>Intelligently pause or redirect CI/CD execution flows by verifying the existence of active Pull Requests.</i></p>
</div>

---

> [!CAUTION]
> The **Gate Check (Open PR)** action is a flow-control primitive. It prevents redundant or dangerous pipeline executions (like triggering an auto-deploy) if the current working branch already has an active Pull Request open against the mainline branch.

## 🚀 Key Impact

- **🛑 Execution Gating**: Conditionally abort workflows or skip subsequent steps based on PR status.
- **🔄 Conditional Routing**: Allows your pipeline to dynamically change behavior (e.g., skip deployments but run tests) if a PR is detected.
- **⚡ Zero Dependency**: Uses standard GitHub CLI (`gh`) out of the box with `ubuntu-latest` runners.

## 🚀 Quick Start

Drop this snippet into your flow-control workflow:

```yaml
steps:
  - name: 🛑 Check if PR is Open
    id: check_pr
    uses: carlos-camara/qa-hub-actions/gate-check-pr@main
    with:
      github-token: ${{ secrets.GITHUB_TOKEN }}
      head-branch: ${{ github.ref_name }}
      base-branch: 'main'
      fail-on-missing: 'false'

  - name: 🚀 Conditional Execution
    if: steps.check_pr.outputs.pr-exists == 'false'
    run: echo "No PR open. Safe to proceed with auto-merge."
```

## ⚙️ Configuration

| Input | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `github-token` | GitHub Token to authenticate with CLI. | **Yes** | N/A |
| `head-branch` | Head branch to check for (e.g., `feature/foo`). | **Yes** | N/A |
| `base-branch` | Base branch the PR would target. | No | `main` |
| `fail-on-missing` | Fail the step (exit 1) if no PR is found. | No | `false` |

## 📤 Outputs

| Output | Description |
| :--- | :--- |
| `pr-exists` | `"true"` if an open PR exists, `"false"` otherwise. |
| `pr-number` | The numerical ID of the found PR (if any). |
