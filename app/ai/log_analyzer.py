class LogAnalyzer:
    def detect_anomalies(self, logs):
        anomalies = []
        for line in logs:
            if "ERROR" in line or "CRITICAL" in line:
                anomalies.append(line)
        return anomalies
