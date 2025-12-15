import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_FILE = "system_metrics.db"

# Load data from the SQLite database
conn = sqlite3.connect(DB_FILE)
df = pd.read_sql(("SELECT * FROM metrics"), conn)
conn.close()

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Plot CPU Usage
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["cpu"], label="CPU Usage (%)", color="green")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Memory Usage
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["memory"], label="Memory Usage (%)", color="red")
plt.xlabel("Time")
plt.ylabel("Memory Usage (%)")
plt.title("Memory Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Disk Usage
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["disk"], label="Disk Usage (%)", color="blue")
plt.xlabel("Time")
plt.ylabel("Disk Usage (%)")
plt.title("Disk Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

