# 🎨 Visual Regression Manager

Automate the lifecycle of your visual baselines. This action allows you to promote "latest" screenshots from a failing test run to become the new "baselines" with a single click or command.

---

## ✨ Key Features

- **🎯 Precision Promotion**: Automatically maps `*_latest.png` artifacts to their corresponding baseline paths.
- **📦 Artifact Aware**: Downloads screenshots directly from any specific Workflow Run ID.
- **🤖 Driver Context**: Handles driver-specific prefixes (e.g., `chrome_`, `playwright_`) to ensure multi-browser stability.
- **🚀 Automated Deployment**: Commits and pushes the new baselines directly to your branch, skipping CI to avoid loops.

---

## 🚀 Usage

### Manual Approval Workflow

Create a file named `.github/workflows/promote-baselines.yml` in your project:

```yaml
name: Promote Visual Baselines

on:
  workflow_dispatch:
    inputs:
      run_id:
        description: 'ID of the run with visual changes to approve'
        required: true

permissions:
  contents: write

jobs:
  promote:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Update Baselines
        uses: carlos-camara/qa-hub-actions/visual-regression-manager@main
        with:
          run-id: ${{ github.event.inputs.run_id }}
          github-token: ${{ secrets.GITHUB_TOKEN }}
          driver-type: 'chrome' # Match your test config
```

---

## 🏗️ How it Works

1. **Input**: You provide the ID of a failed test run that contains the visual changes you want to accept.
2. **Download**: The action fetches the `gui-screenshots` artifact from that run.
3. **Map**: It identifies files like `dashboard_latest.png` and maps them to `baselines/chrome_dashboard.png`.
4. **Update**: It overwrites the old baselines with the new approved images.
5. **Push**: It commits the changes back to the repository.

---

## 📄 Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `run-id` | **Required**. The ID of the workflow run to fetch screenshots from | - |
| `github-token` | **Required**. GitHub token with write permissions | - |
| `screenshots-artifact-name` | Name of the artifact containing screenshots | `gui-screenshots` |
| `baseline-path` | Path to store baselines in the repo | `features/resources/screenshots/baselines` |
| `driver-type` | Driver prefix (chrome, playwright, etc.) | `chrome` |
