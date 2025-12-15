import streamlit as st
import pandas as pd
import sqlite3

st.title("System Monitoring Dashboard")

conn = sqlite3.connect("metrics.db")
df = pd.read_sql("SELECT * FROM metrics", conn)

st.subheader("Current Metrics")
st.metric("CPU Usage (%)", round(df["cpu"].iloc[-1], 2))
st.metric("Memory Usage (%)", round(df["memory"].iloc[-1], 2))
st.metric("Disk Usage (%)", round(df["disk"].iloc[-1], 2))

st.subheader("CPU Usage Over Time")
st.line_chart(df.set_index("timestamp")["cpu"])

st.subheader("Memory Usage Over Time")
st.line_chart(df.set_index("timestamp")["memory"])

st.subheader("Disk Usage Over Time")
st.line_chart(df.set_index("timestamp")["disk"])