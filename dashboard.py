import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="System Monitoring Dashboard", layout="wide")
st.title("System Monitoring Dashboard")

# Absolute path to database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "system_metrics.db")

# --- Safety checks ---
if not os.path.exists(DB_PATH):
    st.error("Database not found. Please run collector.py first.")
    st.stop()

conn = sqlite3.connect(DB_PATH)

# Check if table exists
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='metrics';",
    conn
)

if tables.empty:
    st.error("'metrics' table not found. Run collector.py to generate data.")
    conn.close()
    st.stop()

# Load data
df = pd.read_sql("SELECT * FROM metrics", conn)
conn.close()

if df.empty:
    st.warning("No data yet. Let collector.py run longer.")
    st.stop()

# --- Convert timestamp ---
df["timestamp"] = pd.to_datetime(df["timestamp"])

# --- Charts ---
st.subheader("CPU Usage (%)")
st.line_chart(df.set_index("timestamp")["cpu"])

st.subheader("Memory Usage (%)")
st.line_chart(df.set_index("timestamp")["memory"])

st.subheader("Disk Usage (%)")
st.line_chart(df.set_index("timestamp")["disk"])