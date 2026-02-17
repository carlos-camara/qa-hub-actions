# Deploy Reports to S3

Generic composite action for uploading test artifacts to AWS S3 with proper project structure.

## Features

- ✅ Downloads test reports, screenshots, and performance artifacts from workflow runs
- ☁️ Uploads to S3 with organized project-based structure
- 🔧 Configurable upload toggles (reports, screenshots, performance)
- 🌍 Multi-region AWS support

## Usage

```yaml
- name: Deploy Reports to S3
  uses: carlos-camara/qa-hub-actions/deploy-reports-s3@main
  with:
    project-name: "my-project"
    s3-bucket: ${{ secrets.AWS_S3_BUCKET }}
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: "us-east-1"
    run-id: ${{ github.run_id }}
    upload-reports: 'true'
    upload-screenshots: 'true'
    upload-perf: 'true'
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `project-name` | Project identifier for S3 prefix | Yes | - |
| `s3-bucket` | AWS S3 bucket name | Yes | - |
| `aws-access-key-id` | AWS Access Key ID | Yes | - |
| `aws-secret-access-key` | AWS Secret Access Key | Yes | - |
| `aws-region` | AWS Region | No | `us-east-1` |
| `run-id` | GitHub Workflow Run ID | Yes | - |
| `upload-reports` | Upload test reports? | No | `true` |
| `upload-screenshots` | Upload GUI screenshots? | No | `true` |
| `upload-perf` | Upload performance reports? | No | `true` |

## S3 Structure

Files are organized in S3 as:
```
s3://bucket-name/
  └── project-name/
      └── reports/
          ├── test_run/        # Test reports
          ├── screenshots/     # GUI screenshots
          └── performance_run/ # Performance reports
```

## Required Secrets

- `AWS_S3_BUCKET`: Your S3 bucket name
- `AWS_ACCESS_KEY_ID`: AWS credentials
- `AWS_SECRET_ACCESS_KEY`: AWS credentials
- `AWS_REGION`: AWS region (optional)
