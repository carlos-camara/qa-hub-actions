# 🔗 Link Checker

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Scans files for broken links using Lychee. Highly recommended for documentation projects.

## ⚡ Quick Info

- **Category**: Quality & Security
- **Complexity**: Low
- **Version**: v1.0.0

## 🚀 Usage

```yaml
- name: Check Links
  uses: carlos-camara/qa-hub-actions/link-checker@main
  with:
    search-path: "docs/**/*.md"
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `search-path` | Path or pattern to scan. | `'**/*.md'` |
| `fail-on-error` | Fail build if broken links found? | `'true'` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/link-checker/)
