# Dashboard Interpretation
## System Health
- Latency P95 < 300ms → healthy
- Error rate = 0% → stable
- Drift score < 0.5 → no urgent risk

## Bottlenecks
- Traffic spikes may increase latency

## Alert Triggers
- Error rate > 1% → critical
- Latency P95 > 500ms → warning
- Drift score > 0.5 → critical
