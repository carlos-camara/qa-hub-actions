# 🤖 Action: PR Summarizer

> Deep technical analysis and aesthetic summaries for Pull Requests.

## 🌟 Key Features

- **Deep Technical Analysis**:
  - **🌐 API Footprint**: Detects new/modified routes (Express, Flask, etc.).
  - **🏗️ Structural Impact**: Identifies new functions and classes with `[NEW]` and `[MOD]` badges.
  - **🎯 Locator Diffing**: Highlights exactly which UI locators were updated in `.yaml` files.
  - **✨ BDD Intelligence**: Extracts new Gherkin scenarios and quality tags (`@smoke`, `@critical`).
- **Aesthetic Refinement**:
  - **📊 Impact Analysis**: Dynamic metrics table with visual intensity bars (█).
  - **Premium Iconography**: High-fidelity emojis and grouped technical insights.
  - **Status Badges**: Standardized `[NEW]`, `[MOD]`, and `[FIX]` markers.
- **Breaking Change Detection**: Flags deleted functions or classes with `[!CAUTION]` alerts.

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

## 📊 Output Example

The action will inject a structured block into your template like this:

### 🏗️ Technical Details
**🌐 API Footprint**
- `POST` `/api/incidents`
**🏗️ Structural Impact**
- `[NEW]` `verify_logic`
**🎯 Locator Updates**
- `[MOD]` `login_button`

---
### 📊 Impact Analysis
| Category | Scope | Status |
| :--- | :---: | :--- |
| Backend | 5 | █████ |
| QA | 8 | ████████ |

---
<div align="center">
  <i>Part of the <b>QA Hub Actions</b> Ecosystem</i>
</div>
