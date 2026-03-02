from prometheus_client import start_http_server, Gauge

ping_metric = Gauge("ping_status", "Ping status", ["host"])
sla_metric = Gauge("sla_percentage", "SLA %", ["service"])

def start():
    start_http_server(9100)

def update_ping(host, value):
    ping_metric.labels(host=host).set(1 if value else 0)

def update_sla(service, value):
    sla_metric.labels(service=service).set(value)
