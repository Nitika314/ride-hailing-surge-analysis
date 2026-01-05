import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

st.set_page_config(page_title="Ride-Hailing Surge Pricing", layout="wide")

st.title("🚕 Ride-Hailing Surge Pricing Analysis")

df = pd.read_csv("data/ride_hailing_data.csv", parse_dates=["datetime"])

df["hour"] = df["datetime"].dt.hour
df["dayofweek"] = df["datetime"].dt.dayofweek
df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)
df["is_peak_hour"] = df["hour"].isin([7, 8, 9, 17, 18, 19, 20]).astype(int)
df["surge_pct"] = (df["price_multiplier"] - 1) * 100

# -----------------------------
# KPI SECTION
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Average Surge %", f"{df['surge_pct'].mean():.2f}%")
col2.metric("Peak Hour Surge %", f"{df[df['is_peak_hour']==1]['surge_pct'].mean():.2f}%")
col3.metric("Max Surge %", f"{df['surge_pct'].max():.2f}%")

# -----------------------------
# PEAK VS NON-PEAK
# -----------------------------
st.subheader("Peak vs Non-Peak Surge Pricing")

fig1, ax1 = plt.subplots()
sns.boxplot(x="is_peak_hour", y="surge_pct", data=df, ax=ax1)
ax1.set_xlabel("Peak Hour (1 = Peak)")
ax1.set_ylabel("Surge %")
st.pyplot(fig1)

# -----------------------------
# CORRELATION
# -----------------------------
st.subheader("Traffic & Weather Impact")

corr_features = ["surge_pct", "traffic_index", "rain_intensity", "temperature"]
fig2, ax2 = plt.subplots()
sns.heatmap(df[corr_features].corr(), annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

# -----------------------------
# HYPOTHESIS TEST
# -----------------------------
st.subheader("Weekday vs Weekend Statistical Test")

weekday = df[df["is_weekend"] == 0]["surge_pct"]
weekend = df[df["is_weekend"] == 1]["surge_pct"]

t_stat, p_val = ttest_ind(weekday, weekend, equal_var=False)

st.write(f"T-statistic: {t_stat:.2f}")
st.write(f"P-value: {p_val:.5f}")

if p_val < 0.05:
    st.success("Statistically significant difference detected.")
else:
    st.info("No statistically significant difference detected.")
