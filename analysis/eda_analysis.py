
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(r"E:\PROJects\files\ride_hailing_data.csv", parse_dates=["datetime"])

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
df["hour"] = df["datetime"].dt.hour
df["dayofweek"] = df["datetime"].dt.dayofweek
df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)

df["is_peak_hour"] = df["hour"].isin([7, 8, 9, 17, 18, 19, 20]).astype(int)

# Surge percentage
df["surge_pct"] = (df["price_multiplier"] - 1) * 100

# -----------------------------
# PEAK VS NON-PEAK ANALYSIS
# -----------------------------
peak_surge = df[df["is_peak_hour"] == 1]["surge_pct"].mean()
non_peak_surge = df[df["is_peak_hour"] == 0]["surge_pct"].mean()

print(f"Peak Hour Surge: {peak_surge:.2f}%")
print(f"Non-Peak Surge: {non_peak_surge:.2f}%")

# -----------------------------
# CORRELATION ANALYSIS
# -----------------------------
corr_features = [
    "surge_pct",
    "traffic_index",
    "rain_intensity",
    "temperature"
]

corr_matrix = df[corr_features].corr()

plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation: Traffic, Weather & Surge Pricing")
plt.show()

# -----------------------------
# HYPOTHESIS TESTING
# -----------------------------
weekday_surge = df[df["is_weekend"] == 0]["surge_pct"]
weekend_surge = df[df["is_weekend"] == 1]["surge_pct"]

t_stat, p_value = ttest_ind(weekday_surge, weekend_surge, equal_var=False)

print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.5f}")

if p_value < 0.05:
    print("Significant weekday vs weekend surge difference.")
else:
    print("No significant difference detected.")
