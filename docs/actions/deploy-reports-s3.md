# ☁️ Deploy Reports to S3

Securely store and share your test artifacts using AWS S3.

## 📖 Overview

Automates the upload of test reports to an S3 bucket. It handles path structures that include timestamps and branch names for easy historical access.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `aws-access-key-id` | AWS Access Key. | `REQUIRED` |
| `aws-secret-access-key` | AWS Secret Key. | `REQUIRED` |
| `bucket-name` | Target S3 bucket. | `REQUIRED` |
| `local-path` | Path to the reports directory. | `'reports'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/deploy-reports-s3@main
  with:
    bucket-name: "my-qa-reports"
    local-path: "results"
```

---
*Your data, safely stored.*
