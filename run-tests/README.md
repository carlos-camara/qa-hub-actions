# 🧪 Action: Run QA Test Suite

The unified core engine for test orchestration, featuring industrial-grade report consolidation and multi-engine support for API, GUI, and Performance tests.

---

## 🚀 Key Impact

- **🏗️ Industrial Orchestration**: Executes API, GUI, and Performance test suites with standardized control.
- **📊 Intelligent Reporting**: Automatically organizes JUnit XML results into timestamped, project-specific directories.
- **🔄 Surgical Isolation**: Injects dynamic report paths into test engines to prevent cross-run collisions.
- **🩺 Health Integration**: Built-in support for starting background services and performing pre-flight health checks.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `test-command-api` | No | - | Command for API tests (e.g., `pytest`). |
| `test-command-gui` | No | - | Command for GUI tests (e.g., `playwright`). |
| `test-command-performance`| No | - | Command for Performance tests (e.g., `locust`).|
| `project-name` | No | `dashboard` | Project identifier used for report folder naming. |
| `headless` | No | `true` | Run GUI tests in headless mode. |
| `enable-coverage` | No | `false` | Whether to collect and report code coverage. |

> [!IMPORTANT]
> **Dynamic Pathing**: This action automatically appends `--junit-dir` to your test commands to ensure results are archived in unique, project-isolated folders located in `reports/test_run/`.

---

## ⚡ Quick Start

```yaml
- name: 🧪 Run Quality Suites
  uses: carlos-camara/qa-hub-actions/run-tests@main
  with:
    project-name: "core-api"
    test-command-api: "pytest tests/api"
    test-command-gui: "pytest tests/gui"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/run-tests/)
</div>
