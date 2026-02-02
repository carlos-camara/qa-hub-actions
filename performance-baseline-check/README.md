# 📉 Performance Baseline Check

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Status](https://img.shields.io/badge/status-Beta-yellow?style=for-the-badge&logo=none)

**Automatically detect performance regressions by comparing current metrics against established baselines.**

</div>

---

## 🚀 Overview

This action acts as a rigorous quality gate for performance. It compares a JSON file containing current run metrics against a baseline JSON file, calculating the percentage delta. If performance degrades beyond a specified threshold (e.g., 10%), the action can fail the build or issue a warning.

### Key Features
- **📊 Delta Calculation**: Automatically computes percentage change for all matching keys.
- **🚫 Threshold Enforcement**: Fails the CI pipeline if regression > threshold.
- **📝 Summary Output**: Posts a comparison table to the GitHub Job Summary.

## 🛠️ Usage

```yaml
- uses: carlos-camara/qa-hub-actions/performance-baseline-check@v1
  with:
    current-metrics: 'results/perf.json'
    baseline-metrics: 'baseline/perf.json'
    threshold: '10' # 10% allowed regression
```

## ⚙️ Inputs

| Name | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `current-metrics` | **REQUIRED**. Path to current JSON metrics. | **Yes** | - |
| `baseline-metrics` | **REQUIRED**. Path to baseline JSON metrics. | **Yes** | - |
| `threshold` | Max allowed percentage degradation (e.g., 10). | No | `10` |
| `failure-exit-code` | Exit code to return on regression (0 to warn only). | No | `1` |

---
<div align="center">
  <sub>Powered by QA Hub Actions Ecosystem</sub>
</div>
