# ☁️ Deploy QA Reports to S3

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Stable-success?style=for-the-badge&logo=none)

**Archive your test reports and artifacts to AWS S3 for long-term storage and compliance.**

</div>

---

## 🚀 Overview

This action downloads test artifacts from a GitHub Workflow run and syncs them to a specified AWS S3 bucket. It organizes reports by project and type, ensuring a structured historical record of your quality gates.

### Key Features
- **📦 Artifact Retrieval**: Automatically downloads artifacts from the specified run ID.
- **🗂️ Structured Storage**: Organizes files into a unified test report structure and `performance` folders.
- **🔒 Secure Transfer**: Uses standard AWS credentials for authentication.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/deploy-reports-s3@v1
  with:
    project-name: 'my-dashboard-project'
    s3-bucket: 'my-qa-reports-bucket'
    run-id: ${{ github.run_id }}
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `project-name` | **REQUIRED**. Project identifier used as the S3 subfolder. | **Yes** | - |
| `s3-bucket` | **REQUIRED**. Name of the target S3 bucket. | **Yes** | - |
| `run-id` | **REQUIRED**. The GitHub Run ID to download artifacts from. | **Yes** | - |
| `aws-access-key-id` | **REQUIRED**. AWS Access Key ID. | **Yes** | - |
| `aws-secret-access-key` | **REQUIRED**. AWS Secret Access Key. | **Yes** | - |
| `aws-region` | AWS Region of the bucket. | No | `us-east-1` |
| `upload-reports` | Toggle upload of test reports (consolidated). | No | `true` |
| `upload-screenshots` | Toggle upload of GUI screenshots. | No | `true` |
| `upload-perf` | Toggle upload of Performance reports. | No | `true` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
