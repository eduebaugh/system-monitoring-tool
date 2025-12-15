# System Monitoring & Anomaly Detection Tool

This is my Python-based system monitoring application that collects CPU, memory, and disk utilization metrics, stores time-series data in a SQLite database, detects anomalous system behavior, and visualizes performance trends.

This project demonstrates practical skills in data analytics, IT systems monitoring, and security-oriented anomaly detection.

---

## Features

- Collects real-time system metrics using `psutil`
- Stores historical data in a SQLite database
- Performs threshold-based anomaly detection for:
  - CPU usage
  - Memory usage
  - Disk utilization
- Visualizes system performance trends using Matplotlib
- Exports anomalous events for further investigation

---

## Project Structure

system-monitoring-tool/
│
├── collector.py      # Collects system metrics and stores them in SQLite
├── analyze.py        # Detects anomalous system behavior
├── visualize.py     # Generates performance visualizations
├── requirements.txt # Python dependencies
├── README.md
└── venv/             # Virtual environment (not committed)

## Running with Docker

This project can be built and run using Docker to ensure a consistent and reproducible environment.

### Prerequisites
- Docker Desktop (Windows / macOS / Linux)
- Docker daemon running

### Build the Docker Image
From the project root directory:

```bash
docker build -t system-monitor .