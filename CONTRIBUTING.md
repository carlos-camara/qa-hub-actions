# 🤝 Contributing to QA Hub Actions

Thank you for your interest in contributing to the **QA Hub Actions** ecosystem! 🚀

We are building the industry standard for **Enterprise Quality Orchestration**. To maintain this high standard, we ask that all contributors follow these professional guidelines.

---

## 🏗️ Repository Structure

This is a **monorepo** containing multiple high-performance composite actions. Each action resides in its own dedicated directory:

```text
qa-hub-actions/
├── setup-environment/   # Action: Setup Env 🐍
│   ├── action.yml       # Logic & Metadata
│   └── README.md        # Technical Documentation
├── run-tests/           # Action: Run Tests 🧪
└── ...
```

---

## 🛠️ Development Workflow

1. **Fork & Clone**: Fork the repository and clone it to your local environment.
2. **Branching**: Create a focused feature branch: `git checkout -b feat/my-new-action`.
3. **Development**:
    - If modifying an existing action, edit its `action.yml`.
    - If creating a new action, create a new folder and follow the **Action Standard** below.
4. **Documentation**: Update the `README.md` within the action's folder (see **Gold Standard**).
5. **Commitment**: Use [Conventional Commits](https://www.conventionalcommits.org/):
    - `feat: add new input to setup-environment`
    - `fix: resolve caching issue in run-tests`
    - `docs: update examples`
6. **Pull Request**: Submit a PR to `main` with a clear description of the impact.

---

## 💎 Action Standard (Definition of Done)

Every action in this ecosystem must meet the following technical and aesthetic criteria:

### 1. Metadata (`action.yml`)
- **Name**: Clear, professional name (e.g., "Run QA Test Suite").
- **Description**: Concise summary starting with a relevant emoji.
- **Branding**: Must define `icon` and `color`.
  - *Preferred Colors*: `blue`, `purple`, or `green`.
- **Inputs**: All inputs must have detailed descriptions and sensible defaults.

### 2. Documentation (`README.md`)
Must strictly follow the **Gold Standard Template**:
- **Title**: `# [Icon] Action: [Name]`
- **Hero**: One-line value proposition using relevant emoji.
- **Impact**: Bullet points explaining the technical and business value.
- **Configuration**: Markdown table of Inputs with clear types and defaults.
- **Quick Start**: Clean, copy-pasteable YAML snippet.

### 3. Engineering Excellence
- **Idempotency**: Actions must be safe to run multiple times without side effects.
- **Performance**: Minimize initialization time; utilize caching where possible.
- **Isolation**: Use temporary directories and clean up artifacts.

---

## 🧪 Verification & Testing

Before submitting your contribution:
1. **Linting**: Ensure your YAML and Markdown files comply with our linting standards.
2. **Dry Run**: Test your action in a controlled workflow to verify input/output behavior.
3. **Icons**: Verify that the step names in your `action.yml` use the repository's standard emoji set.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the [MIT License](./LICENSE).

---

<div align="center">
  <i>Let's build the future of Quality Automation together.</i>
</div>
