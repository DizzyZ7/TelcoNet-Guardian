# 🚀 TelcoNet Guardian
### Ultra Enterprise Network Automation & Packet Core Monitoring Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/AsyncIO-Enabled-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker"/>
  <img src="https://img.shields.io/badge/Kubernetes-Supported-326ce5?style=for-the-badge&logo=kubernetes"/>
  <img src="https://img.shields.io/badge/Prometheus-Metrics-orange?style=for-the-badge&logo=prometheus"/>
  <img src="https://img.shields.io/badge/Grafana-Dashboard-F46800?style=for-the-badge&logo=grafana"/>
</p>

---

## 🌍 Overview

**TelcoNet Guardian** is a production-grade automation and monitoring platform designed for modern telecom and packet core infrastructures.

It provides:

- 📡 Network availability monitoring
- 🌐 BGP peer validation
- 🛰 SNMP telemetry collection
- 📊 SLA tracking and reporting
- 🧠 AI-based anomaly detection
- 🌍 Auto network topology discovery
- 🔐 ACL and VLAN validation
- 📦 REST API
- 🐳 Docker & Kubernetes deployment
- 📈 Native Prometheus metrics export

Designed for Network DevOps, NOC Automation and Packet Core Engineers.

---

# 🏗 Architecture

Core components:

- Async monitoring engine (asyncio)
- BGP SSH parser
- SNMP polling engine
- SLA tracking module
- EPC logical validator
- Topology builder
- Prometheus exporter
- FastAPI REST service
- Telegram alert integration
- Docker containerization
- Kubernetes deployment support

---

# 📁 Project Structure

```
telconet-guardian/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── logger.py
│   │
│   ├── monitoring/
│   ├── telemetry/
│   ├── epc/
│   ├── topology/
│   ├── security/
│   ├── ai/
│   ├── api/
│   └── integrations/
│
├── dashboards/
├── k8s/
├── config/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# 🔥 Features

## 📡 Network Monitoring

- ICMP Ping
- TCP Port Checks
- BGP Peer Status Validation
- SNMP Interface Polling

## 📊 SLA Engine

- Uptime calculation
- Failure tracking
- SLA percentage metrics
- Prometheus export

## 🛰 EPC Awareness

Logical modeling for:

- MME
- SGW
- PGW
- HSS
- PCRF

## 🌍 Auto-Discovery

- SNMP SysName detection
- Peer-based topology generation
- Dynamic topology visualization

## 🧠 AI Anomaly Detection

- Statistical baseline analysis
- 3-sigma deviation detection
- Event anomaly counters

## 🔐 Security Validation

- ACL rule inspection
- VLAN consistency checks

---

# 📈 Observability

## Prometheus Metrics

Available at:

```
http://localhost:9100/metrics
```

Exported metrics include:

- ping_status
- bgp_status
- interface_oper_status
- sla_percentage
- anomaly_events

---

## Grafana Dashboard

Import dashboard file:

```
dashboards/grafana_dashboard.json
```

Includes panels for:

- Ping health
- BGP peer state
- SLA percentage
- Interface status
- Anomaly counters

---

# 🚀 Quick Start

## Local Run

```
pip install -r requirements.txt
python app/main.py
```

API endpoint:

```
http://localhost:8000/status
```

---

## Docker Run

```
docker-compose up --build
```

---

## Kubernetes Deployment

```
kubectl apply -f k8s/
```

---

# ⚙ Configuration

Edit:

```
config/devices.yaml
```

Example:

```yaml
devices:
  - name: core-router-1
    ip: 10.0.0.1
    community: public
    peers:
      - core-router-2
```

---

# 🧪 CI/CD

GitHub Actions workflow:

```
.github/workflows/ci.yml
```

Pipeline includes:

- Docker build validation
- Project structure verification
- Deployment preparation

---

# 🏆 Production Highlights

✔ Async-first architecture  
✔ Micro-modular design  
✔ Dockerized services  
✔ Kubernetes scalable  
✔ Prometheus-native monitoring  
✔ AI anomaly detection  
✔ Auto-discovery support  
✔ EPC-aware monitoring  
✔ Enterprise-ready CI/CD  

---

# 🎯 Designed For

- Network DevOps Engineers
- Packet Core Engineers
- NOC Automation Specialists
- BGP Infrastructure Engineers
- Telecom Infrastructure Teams

---

# 📌 Roadmap

- Multi-region support
- PostgreSQL persistence layer
- Redis caching
- Web UI
- RBAC implementation
- Event correlation engine
- ML-powered anomaly detection

---

# 👨‍💻 Author

Dimash "DizZy"  
Network Automation & Telco Engineering

---

# ⭐ Support

If you find this project useful:

- Star the repository
- Fork it
- Deploy it
- Improve it
- Automate everything
