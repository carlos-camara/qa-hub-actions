# 📉 Performance Baseline Check

> Part of the [QA Hub Actions](https://github.com/carlos-camara/qa-hub-actions) ecosystem.

Compare current performance metrics against a baseline and fail on regressions automatically.

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
