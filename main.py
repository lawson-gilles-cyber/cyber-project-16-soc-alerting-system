# SOC Alerting System

from core.detector import analyze_log
from core.notifier import send_alert

# Load logs
with open("data/logs.txt", "r") as file:
    logs = file.readlines()

print("=== SOC Alerting System ===\n")

# Process logs
for log in logs:
    log = log.strip()

    alert = analyze_log(log)

    if alert:
        # Send alert (log + console)
        send_alert(alert)
