# 🔗 Link Checker

!!! info "At a Glance"
    - **Category**: Quality & Security
    - **Complexity**: Low
    - **Version**: v1.0.0 (Stable)
    - **Primary Tool**: Lychee

Maintain a high-quality documentation site by automatically checking for broken links.

## 📖 Overview

Uses `Lychee` to scan your Markdown files and documentation for broken URLs. Perfect for preventing "404 Not Found" errors in your Wikis and READMEs.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `search-path` | Glob pattern to find files to scan. | `'**/*.md'` |
| `fail-on-error` | Whether to fail the build on broken links. | `'true'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/link-checker@main
  with:
    search-path: "docs/**/*.md"
```

---
*Clean links, happy users.*
