# 🎯 Action: PR Milestoner

> Automatically assigns the latest open milestone to a Pull Request.

## 📖 What it does
- **Smart Assignment**: Fetches open milestones from the repository.
- **Strategy Support**: Choose between `latest_created` (default) or `next_due`.
- **Zero Config**: Works out of the box with standard GitHub milestones.

## 🛠️ Configuration
| Input | Description | Default |
| :--- | :--- | :--- |
| `github-token` | `REQUIRED` | Token for API access. |
| `strategy` | `latest_created` | Milestone selection logic. |

## 🚀 Usage

```yaml
- uses: carlos-camara/qa-hub-actions/pr-milestoner@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    strategy: "next_due"
```
