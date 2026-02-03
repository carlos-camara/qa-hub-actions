# ☁️ Deploy QA Reports to S3

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Downloads standard QA Hub test reports and deploys them to AWS S3.

## ⚡ Quick Info

- **Category**: Reporting & Notifications
- **Complexity**: Medium
- **Version**: v2.1.0

## 🚀 Usage

```yaml
- uses: carlos-camara/qa-hub-actions/deploy-reports-s3@main
  with:
    project-name: "dashboard"
    s3-bucket: "my-qa-reports-bucket"
    aws-access-key-id: ${{ secrets.AWS_KEY }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET }}
    run-id: ${{ github.run_id }}
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `project-name` | Project subfolder in S3. | `REQUIRED` |
| `s3-bucket` | Target S3 bucket name. | `REQUIRED` |
| `aws-access-key-id` | AWS Access Key. | `REQUIRED` |
| `aws-region` | AWS Region. | `'us-east-1'` |
| `run-id` | Workflow Run ID to download from. | `REQUIRED` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/deploy-reports-s3/)
