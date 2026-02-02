# Contributing to QA Hub Actions

First off, thank you for considering contributing to QA Hub Actions! It's people like you that make QA Hub such a great tool.

## 🛠 Development Workflow

1.  **Fork the repo** and create your branch from `main`.
2.  **Make your changes**. If you are adding a new action, follow the existing structure (root-level folder, `action.yml`, and `README.md`).
3.  **Validate**. Ensure your `action.yml` is well-formatted and includes branding (icon and color).
4.  **Issue a Pull Request**. Provide a clear description of the changes or the new action.

## 📝 Coding Standards

- **Naming**: Use kebab-case for input names and action folder names.
- **Shell**: Use `bash` for cross-platform compatibility in composite steps where possible, or `pwsh` if specific Windows/PowerShell features are needed.
- **Documentation**: Every action MUST have its own `README.md` with clear input/output descriptions and usage examples.

## ⚖️ License

By contributing, you agree that your contributions will be licensed under its [MIT License](LICENSE).

---

<p align="center">
  <b>Happy Testing!</b>
</p>
