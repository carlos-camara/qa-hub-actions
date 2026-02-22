# 🔗 Action: Link Checker

<div align="center">
  <p><i>Maintain a high-quality documentation site by automatically detecting and reporting broken links.</i></p>
</div>

---

> [!TIP]
> Use the **Link Checker** as part of your documentation CI to ensure that every link in your `docs/` and `READMEs` remains valid, preventing the frustration of "404 Not Found" for your users.

## 🚀 Key Impact

- **🔍 Comprehensive Scanning**: Recursively checks Markdown and HTML files for broken internal and external links.
- **🛠️ Flexible Filtering**: Use glob patterns to focus the scan on specific documentation directories.
- **🛑 Failure Guardrails**: Configure the action to fail the build if any broken links are detected.

---

## ⚙️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `search-path` | No | `**/*.md` | Glob pattern to find files to scan. |
| `fail-on-error` | No | `true` | Whether to fail the build on broken links. |

---

## ⚡ Quick Start

```yaml
- name: 🔗 Check Documentation Links
  uses: carlos-camara/qa-hub-actions/link-checker@main
  with:
    search-path: "docs/**/*.md"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/link-checker/)
</div>
