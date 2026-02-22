# 📉 Action: Performance Baseline

<div align="center">
  <p><i>Protect your user experience by automatically detecting latency regressions and generating high-fidelity visual trend charts.</i></p>
</div>

---

> [!IMPORTANT]
> The **Performance Baseline** action provides structural performance guarantees. It actively compares incoming latency footprints against a gold-standard benchmark file, automatically failing PRs that exceed the calculated drift tolerance limits.

## 🚀 Key Impact

- **🩺 Regression Guardrails**: Compares current performance metrics (Locust/Playwright) against a baseline JSON with configurable drift tolerance.
- **📊 Aesthetic reporting**: Automatically generates Mermaid `xychart-beta` visualizations directly in your GitHub Job Summary.
- **🚫 Automated Gates**: Fails the CI pipeline with custom exit codes if performance deviates beyond the allowed threshold.
- **🏗️ Zero Configuration**: Works with any standard flat JSON metric object `{ "metric_name": value }`.

---

## 🛠️ Configuration

| Input | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `current-metrics` | **Yes** | - | Path to the latest performance JSON report. |
| `baseline-metrics` | **Yes** | - | Path to the gold-standard baseline JSON. |
| `threshold` | No | `10` | Frequency percentage allowed for drift (e.g., `5` for 5%). |
| `failure-exit-code` | No | `1` | Exit code to return if regression threshold is met. |

---

## ⚡ Quick Start

Drop this snippet into your pipeline:

```yaml
steps:
  - name: 📉 Performance Baseline Check
    uses: carlos-camara/qa-hub-actions/performance-baseline-check@main
    with:
      current-metrics: "results/perf_metrics.json"
      baseline-metrics: "perf_baseline.json"
      threshold: "10"
```

---

<div align="center">
  [View Full Wiki](https://carlos-camara.github.io/qa-hub-actions/actions/performance-baseline-check/)
</div>
