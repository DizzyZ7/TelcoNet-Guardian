from prometheus_client import start_http_server, Gauge, Counter

ping_metric = Gauge("ping_status", "Ping status", ["host"])
bgp_metric = Gauge("bgp_status", "BGP peer status", ["host"])
interface_metric = Gauge("interface_oper_status", "Interface status", ["host"])
anomaly_metric = Counter("anomaly_events", "Detected anomalies")

def start():
    start_http_server(9100)

def update_ping(host, value):
    ping_metric.labels(host=host).set(1 if value else 0)

def update_sla(service, value):
    sla_metric.labels(service=service).set(value)
