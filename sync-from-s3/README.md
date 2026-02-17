# Sync from S3 to Repository

Generic composite action for downloading files from AWS S3 and committing them to your repository.

## Features

- ☁️ Downloads files from S3 with project-based structure
- 📦 Automatically commits changes to your repository
- 🔧 Configurable paths and commit messages
- 🌍 Multi-region AWS support

## Usage

```yaml
- name: Sync Reports from S3
  uses: carlos-camara/qa-hub-actions/sync-from-s3@main
  with:
    project-name: "my-project"
    s3-bucket: ${{ secrets.AWS_S3_BUCKET }}
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: "us-east-1"
    target-path: "reports/"
    s3-path: "reports/"
    commit-message: "chore: sync from S3 [skip ci]"
    branch: "main"
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `project-name` | Project identifier for S3 prefix | Yes | - |
| `s3-bucket` | AWS S3 bucket name | Yes | - |
| `aws-access-key-id` | AWS Access Key ID | Yes | - |
| `aws-secret-access-key` | AWS Secret Access Key | Yes | - |
| `aws-region` | AWS Region | No | `us-east-1` |
| `target-path` | Local path to sync files to | Yes | - |
| `s3-path` | S3 path suffix after project name | No | `reports/` |
| `commit-message` | Git commit message | No | `chore: sync from S3 [skip ci]` |
| `branch` | Target branch for commit | No | `main` |

## Use Cases

### Test Report Synchronization
Perfect for pulling test results from S3 into your repository for display on GitHub Pages:

```yaml
on:
  workflow_run:
    workflows: ["Deploy Reports to S3"]
    types: [completed]

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: carlos-camara/qa-hub-actions/sync-from-s3@main
        with:
          project-name: "dashboard"
          s3-bucket: ${{ secrets.AWS_S3_BUCKET }}
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          target-path: "reports/test_run"
```

## Required Secrets

- `AWS_S3_BUCKET`: Your S3 bucket name
- `AWS_ACCESS_KEY_ID`: AWS credentials
- `AWS_SECRET_ACCESS_KEY`: AWS credentials
- `AWS_REGION`: AWS region (optional)
