
from prometheus_client import Counter, Gauge, Histogram
request_count = Counter("model_requests_total", "Total API requests", ["endpoint"])
request_latency = Histogram("model_request_latency_seconds", "Request latency", ["endpoint"])
error_rate = Gauge("model_error_rate", "API error rate")
drift_score = Gauge("data_drift_score", "Data drift score", ["feature"])
