# <div align="center">🏷️ Action: PR Labeler</div>

<div align="center">
  <p><i>Automatically categorize Pull Requests based on modified file paths to maintain repository hygiene and streamline code reviews.</i></p>
</div>


---

## 🚀 Key Impact

- **🏷️ Automated Triage**: Tags PRs with relevant labels (e.g., `Frontend`, `Backend`, `DevOps`) based on path matching rules.
- **🔄 State Synchronization**: Option to automatically remove labels if the relevant files are removed from the PR.
- **🏗️ Centralized Config**: Define all labeling rules in a single, professional `.github/labeler.yml` file.
- **✨ Zero Overhead**: High-performance execution that keeps your repository organized without manual effort.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `repo-token` | No | `${{ github.token }}` | GitHub Token for applying labels. |
| `configuration-path` | No | `.github/labeler.yml` | Path to the YAML file defining labeling rules. |
| `sync-labels` | No | `true` | Remove labels when files no longer match rules. |

---

## ⚡ Quick Start

```yaml
- name: 🏷️ Triage PR
  uses: carlos-camara/qa-hub-actions/pr-labeler@main
  with:
    repo-token: ${{ secrets.GITHUB_TOKEN }}
    configuration-path: ".github/labeler.yml"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/pr-labeler/)
</div>
