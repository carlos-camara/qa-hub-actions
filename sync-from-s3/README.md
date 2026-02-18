# 🔄 Action: Sync from S3

Generic cloud-to-local synchronization for downloading files from AWS S3 and automatically committing them to your repository.

---

## 🚀 Key Impact

- **☁️ Cloud-to-Repo Sync**: Efficiently downloads artifacts from S3 using optimized synchronization logic.
- **💾 Automated Commits**: Automatically stages, commits, and pushes downloaded files back to your repository branch.
- **⚡ Surgical Incrementality**: Automatically skips already existing local directories, reducing sync time and network overhead.
- **🛡️ History Preservation**: Explicitly avoids the `--delete` flag to ensure historical data in the repo is never wiped by S3 rotation.
- **🏗️ Project Sharding**: Supports project-based S3 prefixes to maintain isolation across multi-project environments.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `project-name` | **Yes** | - | Unique identifier for the project sharding. |
| `s3-bucket` | **Yes** | - | Target AWS S3 bucket name. |
| `target-path` | **Yes** | - | Local directory to sync files into. |
| `aws-access-key-id` | **Yes** | - | AWS Authentication Key. |
| `aws-secret-access-key`| **Yes** | - | AWS Authentication Secret. |
| `s3-path` | No | `reports/` | S3 path suffix after the project name. |
| `commit-message` | No | `chore: sync` | Custom Git commit message. |

---

## ⚡ Quick Start

```yaml
- name: 🔄 Sync Reports from Cloud
  uses: carlos-camara/qa-hub-actions/sync-from-s3@main
  with:
    project-name: "dashboard"
    s3-bucket: "qa-hub-storage"
    aws-access-key-id: ${{ secrets.AWS_KEY }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET }}
    target-path: "docs/reports/"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/sync-from-s3/)
</div>
