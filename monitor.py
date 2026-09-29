import psutil
import json
from datetime import datetime

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Collect system information
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("C:\\").percent

# Create a report
report = {
    "timestamp": timestamp,
    "cpu_usage": cpu_usage,
    "ram_usage": ram_usage,
    "disk_usage": disk_usage
}

# Load existing reports
try:
    with open("health_report.json", "r") as file:
        reports = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    reports = []

# Add new report
reports.append(report)

# Save reports
with open("health_report.json", "w") as file:
    json.dump(reports, file, indent=4)

# Display result
print("System Health Report")
print("--------------------")
print("Timestamp:", timestamp)
print("CPU:", cpu_usage, "%")
print("RAM:", ram_usage, "%")
print("Disk:", disk_usage, "%")
print()
print("Report saved successfully!")