# 📉 Performance Baseline Check

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Compare current performance metrics against a baseline, detect slowdowns, and generate automated Mermaid trend visualizations.

## ✨ Key Features

- **🩺 Drift Detection**: Compares JSON metrics against a baseline with configurable % thresholds.
- **📊 Visual Trends**: Automatically generates a Mermaid `xychart-beta` in the Job Summary.
- **🚫 Automated Guardrails**: Fails the CI pipeline if any metric deviates beyond the allowed drift.

## ⚡ Quick Info

- **Category**: Quality & Security
- **Complexity**: Low
- **Version**: v1.1.0

## 🚀 Usage

```yaml
- uses: carlos-camara/qa-hub-actions/performance-baseline-check@main
  with:
    current-metrics: "results/perf.json"
    baseline-metrics: "baseline/perf.json"
    threshold: "10"
```

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `current-metrics` | Path to current JSON metrics. | `REQUIRED` |
| `baseline-metrics` | Path to baseline JSON metrics. | `REQUIRED` |
| `threshold` | % threshold for regression. | `'10'` |

---
[View Full Documentation](https://carlos-camara.github.io/qa-hub-actions/actions/performance-baseline-check/)
