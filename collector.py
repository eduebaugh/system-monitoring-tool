import psutil
import time
import sqlite3
from datetime import datetime

conn = sqlite3.connect('system_metrics.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    timestamp TEXT,
    cpu REAL,
    memory REAL,
    disk REAL
)
""")

print("Starting system monitoring... Press Ctrl+C to stop")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        timestamp = datetime.now().isoformat()

        cursor.execute(
            "INSERT INTO metrics VALUES (?, ?, ?, ?)",
            (timestamp, cpu, memory, disk)
        )
        conn.commit()

        print(f"{timestamp} | CPU: {cpu}% | MEM: {memory}% | DISK: {disk}%")
        time.sleep(5)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")

finally:
    conn.close()