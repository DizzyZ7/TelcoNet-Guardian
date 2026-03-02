from prometheus_client import start_http_server, Gauge

ping_metric = Gauge("host_ping_status", "Ping status", ["host"])
bgp_metric = Gauge("bgp_status", "BGP status", ["host"])

def start_exporter():
    start_http_server(9100)

def update_ping(host, status):
    ping_metric.labels(host=host).set(1 if status else 0)

def update_bgp(host, status):
    bgp_metric.labels(host=host).set(1 if status else 0)
