# 📉 Performance Baseline

Detect performance regressions by comparing test run metrics against an established baseline.

## 📖 Overview

Calculates the performance delta between the current run and a stored baseline. It helps identify latency jumps or throughput drops before they reach production.

## 🛠️ Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `current-metrics-path` | Path to the current performance JSON. | `REQUIRED` |
| `baseline-path` | Path to the baseline JSON. | `""` |
| `threshold` | Percentage of regression allowed. | `'5'` |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/performance-baseline-check@main
  with:
    current-metrics-path: "results/performance.json"
    threshold: "10"
```

---
*Speed is a feature. Protect it.*
