# Ride-Hailing Surge Pricing Analysis

This project analyzes dynamic surge pricing behavior in ride-hailing services using Python, statistical analysis, and data visualization.  
The goal is to understand how demand patterns, traffic congestion, and weather conditions influence surge pricing.

---

## Key Objectives
- Identify peak-hour surge pricing patterns and quantify surge exceeding 35%
- Analyze the relationship between traffic conditions, weather factors, and surge pricing
- Compare weekday vs weekend surge behavior using statistical hypothesis testing
- Build an interactive dashboard to visualize surge pricing trends

---

## Dataset
The dataset represents simulated ride-hailing trip data with the following features:
- `datetime` – Ride timestamp
- `price_multiplier` – Dynamic pricing multiplier
- `traffic_index` – Traffic congestion level
- `rain_intensity` – Weather impact indicator
- `temperature` – Ambient temperature
- `distance_km` – Trip distance
- `base_fare` – Base ride fare

Synthetic data is used to closely mimic real-world ride-hailing scenarios.

---

## Analysis Performed
- Feature engineering on time-based variables (hour, peak hours, weekends)
- Exploratory data analysis to identify surge patterns
- Correlation analysis between traffic, weather, and surge pricing
- Hypothesis testing (Welch’s t-test) to validate weekday vs weekend differences

---

## Dashboard
An interactive Streamlit dashboard was developed to:
- Display key surge pricing metrics
- Visualize peak vs non-peak surge distribution
- Show correlation heatmaps for traffic and weather impact
- Present statistical test results

---

## Tech Stack
- Python
- Pandas, NumPy
- SciPy
- Matplotlib, Seaborn
- Streamlit

---

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py


