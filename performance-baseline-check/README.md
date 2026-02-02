# 📉 Performance Baseline Check

Prevent performance regressions by comparing current run data against a trusted baseline. If metrics slip beyond your defined threshold, this action will automatically flag the regression.

## 🛠 Features

- **Automated Regression Testing**: Compare latency, throughput, or any numeric metric.
- **Configurable Thresholds**: Set a percentage tolerance (e.g., 10%) before failing.
- **Visual Feedback**: Generates a professional comparison table directly in your GitHub Job Summary.
- **Customizable Failures**: Control whether regressions break the build or purely report data.

## 📥 Inputs

| Name | Description | Default |
| :--- | :--- | :--- |
| `current-metrics` | **Required**. Path to current JSON metrics file. | - |
| `baseline-metrics`| **Required**. Path to baseline JSON metrics file. | - |
| `threshold` | Slowdown percentage to allow (e.g., `10`). | `10` |
| `failure-exit-code`| Exit code if regression detected. | `1` |

## 🚀 Usage

```yaml
- uses: qa-hub-actions/performance-baseline-check@v1
  with:
    current-metrics: "results/perf-run.json"
    baseline-metrics: "perf-targets/baseline.json"
    threshold: 15 # Allow up to 15% regression
```

### JSON Format Example
```json
{
  "search_latency": 145.2,
  "checkout_time": 320.5
}
```

> [!IMPORTANT]
> Ensure your JSON keys match in both baseline and current files for accurate comparison.
