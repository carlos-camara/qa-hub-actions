# 🤖 PR Summarizer

Automatically summarize Pull Request changes following your `.github/pull_request_template.md` structure. This action performs deep structural analysis to provide reviewers with a high-fidelity "TL;DR" of the technical impact.

## 🌟 Key Features

- **Structural Intelligence**: Uses Python's `ast` to detect new functions/classes.
- **BDD Awareness**: Extracts new Gherkin scenarios from `.feature` files.
- **Template Alignment**: Automatically maps findings to your existing PR template sections.
- **Generic & Configurable**: Works across any repo with overridable domain mapping.

## 🚀 Usage

Add this to your PR orchestration workflow (e.g., `.github/workflows/pr_intelligence.yml`):

```yaml
name: PR Intelligence

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Required for git diff analysis

      - name: Generate Summary
        uses: carlos-camara/qa-hub-actions/pr-summarizer@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          target: 'description' # Or 'comment'
```

## 🔧 Inputs

| Input | Description | Required | Default |
| :--- | :--- | :--- | :--- |
| `github-token` | Token for PR description/comment updates. | Yes | - |
| `domain-mapping` | JSON string mapping patterns to domains. | No | `{}` |
| `target` | Where to post (description or comment). | No | `description` |

## ⚖️ How it works

The action performs the following steps:
1. **Scans for Changes**: Analyzes the `git diff` against the base branch.
2. **Deep Analysis**:
    - **Python**: Detects structural changes (functions/classes).
    - **Gherkin**: Extracts new scenarios.
    - **YAML**: Identifies locator updates.
3. **Template Injection**: Matches findings against your `.github/pull_request_template.md` headers.
4. **Publish**: Updates the PR description or adds a comment.

---
<div align="center">
  <i>Part of the <b>QA Hub Actions</b> Ecosystem</i>
</div>
