# 🤝 Contributing to QA Hub Actions

<div align="center">

![Contribution](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)

**First off, thank you for considering contributing to QA Hub Actions! It's people like you that make this ecosystem great.**

</div>

---

## 🛠 Development Workflow

1.  **Fork the repo** and create your branch from `main`.
2.  **Make your changes**. If you are adding a new action, please follow the existing folder structure:
    - Root-level folder (kebab-case)
    - `action.yml` (metadata)
    - `README.md` (documentation)
3.  **Validate**. Ensure your `action.yml` is well-formatted and includes branding (icon and color).
4.  **Issue a Pull Request**. Provide a clear description of the new features or fixes.

## 📝 Coding Standards

- **Naming**: Use `kebab-case` for input names, action folder names, and arguments.
- **Shell**: Use `bash` for cross-platform compatibility in composite steps where possible. Use `pwsh` only if specific Windows features are needed.
- **Documentation**: Every action **MUST** have its own `README.md` with clear `Inputs` table and `Usage` examples.

## ⚖️ License

By contributing, you agree that your contributions will be licensed under its [MIT License](LICENSE).

---

<p align="center">
  <b>Happy Testing!</b>
</p>
