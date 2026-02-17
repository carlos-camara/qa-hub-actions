# ☁️ Action: Deploy Reports to S3

Securely archive and organize industrial-grade QA reports in AWS S3 with project-based isolation and long-term retention.

---

## 🚀 Key Impact

- **📥 Artifact Orchestration**: Automatically downloads test reports, GUI screenshots, and performance data from GitHub Actions.
- **☁️ Cloud-Native Storage**: Syncs artifacts to AWS S3 using short-lived credentials for maximum security.
- **🏗️ Organized Structure**: Enforces a standard project hierarchy in S3 (e.g., `s3://bucket/project/reports/`).
- **🔧 Granular Control**: Toggle synchronization for specific artifact types independently.

---

## 🏗️ S3 Architecture

Files are organized in your bucket as:
```text
s3://bucket-name/
  └── project-name/
      └── reports/
          ├── test_run/        # Unified JUnit XMLs
          ├── screenshots/     # Visual evidence
          └── performance_run/ # Monitoring data
```

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `project-name` | **Yes** | - | Unique identifier for the project. |
| `s3-bucket` | **Yes** | - | Target AWS S3 bucket name. |
| `aws-access-key-id` | **Yes** | - | AWS Authentication Key. |
| `aws-secret-access-key` | **Yes** | - | AWS Authentication Secret. |
| `run-id` | **Yes** | - | GitHub Run ID to pull reports from. |
| `aws-region` | No | `us-east-1` | AWS Infrastructure region. |
| `upload-reports` | No | `true` | Toggle for test report upload. |
| `upload-screenshots` | No | `true` | Toggle for screenshot upload. |
| `upload-perf` | No | `true` | Toggle for performance metadata. |

---

## ⚡ Quick Start

```yaml
- name: ☁️ Deploy Reports to S3
  uses: carlos-camara/qa-hub-actions/deploy-reports-s3@v1
  with:
    project-name: "dashboard"
    s3-bucket: "qa-hub-storage"
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    run-id: ${{ github.run_id }}
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/deploy-reports-s3/)
</div>
