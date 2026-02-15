# Contributing to QA Hub Actions

Thank you for your interest in contributing to the **QA Hub Actions** ecosystem! 🚀

We are building the standard for Enterprise Quality Orchestration on GitHub. To maintain this high standard, we ask that all contributors follow these guidelines.

## 🏗️ Repository Structure

This is a **monorepo** containing multiple composite actions. Each action resides in its own directory:

```text
qa-hub-actions/
├── setup-environment/   # Action: Setup Env
│   ├── action.yml       # Metadata & Logic
│   └── README.md        # Documentation
├── run-tests/           # Action: Run Tests
└── ...
```

## 🛠️ Development Workflow

1.  **Fork & Clone**: Fork the repository and clone it locally.
2.  **Branching**: Create a feature branch: `git checkout -b feat/my-new-action`.
3.  **Development**:
    - If modifying an existing action, edit its `action.yml`.
    - If creating a new action, create a new folder and follow the **Action Standard** below.
4.  **Documentation**: Update the `README.md` within the action's folder.
5.  **Commit**: Use [Conventional Commits](https://www.conventionalcommits.org/):
    - `feat: add new input to setup-environment`
    - `fix: resolve caching issue in run-tests`
    - `docs: update examples`
6.  **Pull Request**: Submit a PR to `main`.

## 💎 Action Standard (Definition of Done)

Every action in this repository must meet the following criteria:

### 1. Metadata (`action.yml`)
- **Name**: Clear, concise name (e.g., "Run QA Test Suite").
- **Description**: Professional summary starting with an emoji.
- **Branding**: Must define `icon` and `color`.
    - *Preferred Color*: `blue`, `purple`, or `green`.
- **Inputs**: All inputs must have descriptions and (where possible) defaults.

### 2. Documentation (`README.md`)
Must use the **Gold Standard Template**:
- **Title**: `# 🔧 Action: [Name]`
- **Hero**: One-line value proposition.
- **What it does**: Bullet points explaining the technical impact.
- **Configuration**: Markdown table of Inputs.
- **Quick Start**: Copy-pasteable YAML snippet.

### 3. Idempotency
Actions should be designed to be idempotent where possible. Ensure that running the action multiple times does not cause failures (e.g., checking if a directory exists before creating it).

## 🧪 Testing

Before submitting:
1.  **Lint**: Run the codebase linter to ensure YAML/Markdown compliance.
2.  **Verify**: If possible, test your action in a private workflow to ensure it executes as expected.

## 📜 License

By contributing, you agree that your contributions will be licensed under the [MIT License](./LICENSE).
