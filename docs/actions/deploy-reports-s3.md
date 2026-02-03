# ☁️ Deploy Reports to S3

!!! info "At a Glance"
    - **Category**: Reporting & Notifications
    - **Complexity**: Medium
    - **Version**: v2.1.0 (Stable)
    - **Primary Tool**: AWS CLI / S3 Sync

Securely store and share your test artifacts using AWS S3.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `project-name` | Name of the project (e.g., `dashboard`). Used as the subfolder in S3. | `REQUIRED` |
| `s3-bucket` | Name of the S3 bucket. | `REQUIRED` |
| `aws-access-key-id` | AWS Access Key ID. | `REQUIRED` |
| `aws-secret-access-key` | AWS Secret Access Key. | `REQUIRED` |
| `aws-region` | AWS Region. | `'us-east-1'` |
| `run-id` | GitHub Workflow Run ID to download artifacts from. | `REQUIRED` |
| `upload-reports` | Upload test reports (consolidated)? | `'true'` |
| `upload-screenshots` | Upload GUI screenshots? | `'true'` |
| `upload-perf` | Upload Performance reports? | `'true'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/deploy-reports-s3@main
  with:
    project-name: "dashboard"
    s3-bucket: "my-qa-reports-bucket"
    aws-access-key-id: ${{ secrets.AWS_KEY }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET }}
    run-id: ${{ github.run_id }}
```

---
*Your data, safely stored.*
