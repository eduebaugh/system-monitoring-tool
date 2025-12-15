import sqlite3
import pandas as pd

DB_FILE = "system_metrics.db"

conn = sqlite3.connect(DB_FILE)

df = pd.read_sql_query("SELECT * FROM metrics", conn)
conn.close()

df["timestamp"] = pd.to_datetime(df["timestamp"])

print("\n=== BASIC SYSTEM STATS ===")
print(df.describe())

# Anomaly Detection
CPU_THRESHOLD = 80

high_cpu = df[df["cpu"] > CPU_THRESHOLD]

print(f"\nHigh CPU Usage Instances (>{CPU_THRESHOLD}%):")
print(high_cpu[["timestamp", "cpu"]].tail())

# Save any anomalies to a separate CSV file

high_cpu.to_csv("high_cpu_usage.csv", index=False)

print("\nAnalysis complete. High CPU usage instances saved to 'high_cpu_usage.csv'.")

# Statistical Anomaly Detection (Z-score)
def detect_anomalies_zscore(df, column, threshold=3):
    mean = df[column].mean()
    std = df[column].std()
    df["z_score"] = (df[column] - mean) / std
    anomalies = df[abs(df["z_score"]) > threshold]
    return anomalies

cpu_anomalies = detect_anomalies_zscore(df, "cpu")
memory_anomalies = detect_anomalies_zscore(df, "memory")
disk_anomalies = detect_anomalies_zscore(df, "disk")

# Printing and saving anomalies
print(f"\nCPU Anomalies Detected (Z-score > 3): {len(cpu_anomalies)} instances")
print(cpu_anomalies[["timestamp", "cpu", "z_score"]].tail())

print(f"\nMemory Anomalies Detected (Z-score > 3): {len(memory_anomalies)} instances")
print(memory_anomalies[["timestamp", "memory", "z_score"]].tail())

print(f"\nDisk Anomalies Detected (Z-score > 3): {len(disk_anomalies)} instances")
print(disk_anomalies[["timestamp", "disk", "z_score"]].tail())

cpu_anomalies.to_csv("cpu_anomalies.csv", index=False)
memory_anomalies.to_csv("memory_anomalies.csv", index=False)
disk_anomalies.to_csv("disk_anomalies.csv", index=False)
print("\nAnomalies saved to 'cpu_anomalies.csv', 'memory_anomalies.csv', and 'disk_anomalies.csv'.")

# Alerting System based on anomalies of CPU, Memory, and Disk
def alert(metric, value, timestamp):
    if value > 95:
        level = "CRITICAL"
    elif value > 85:
        level = "WARNING"
    else:
        return
    print(f"[{level} ALERT] {metric} usage at {value}% on {timestamp}")

for _, row in cpu_anomalies.iterrows():
    alert("CPU", row["cpu"], row["timestamp"])
    alert("Memory", row["memory"], row["timestamp"])
    alert("Disk", row["disk"], row["timestamp"])