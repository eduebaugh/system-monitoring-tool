import psutil
import sqlite3
import time
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "system_metrics.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    timestamp TEXT,
    cpu REAL,
    memory REAL,
    disk REAL
)
""")
conn.commit()

print("Collecting system metrics... Press Ctrl+C to stop.")

try:
    while True:
        timestamp = datetime.now().isoformat()
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        cur.execute(
            "INSERT INTO metrics VALUES (?, ?, ?, ?)",
            (timestamp, cpu, memory, disk)
        )
        conn.commit()

        print(f"{timestamp} | CPU: {cpu}% | MEM: {memory}% | DISK: {disk}%")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")

finally:
    conn.close()