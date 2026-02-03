# 📉 Performance Baseline

!!! info "At a Glance"
    - **Category**: Quality & Security
    - **Complexity**: Low
    - **Version**: v1.1.0 (Stable)
    - **Primary Tool**: Node.js JSON Comparator

Detect performance regressions by comparing test run metrics against an established baseline.

## 🛠️ Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| `current-metrics` | Path to current JSON metrics (e.g., `results/perf.json`). | `REQUIRED` |
| `baseline-metrics` | Path to baseline JSON metrics (e.g., `baseline/perf.json`). | `REQUIRED` |
| `threshold` | Percentage threshold for regression (e.g., `10` for 10% slowdown). | `'10'` |
| `failure-exit-code` | Exit code to return if regression is detected. | `'1' |

## 🚀 Usage Example

```yaml
- uses: carlos-camara/qa-hub-actions/performance-baseline-check@main
  with:
    current-metrics: "results/performance.json"
    baseline-metrics: "baseline/performance.json"
    threshold: "5"
```

---
*Speed is a feature. Protect it.*
