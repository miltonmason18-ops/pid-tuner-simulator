import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Nigeria Inflation Tracker",
    page_icon="🇳🇬",
    layout="wide"
)

st.title("🇳🇬 Nigeria Inflation Rate Tracker")
st.markdown("### Built by Omotoso Odunayo")

# --- Data ---
years = [2019, 2020, 2021, 2022, 2023, 2024]
rates = [11.40, 13.25, 16.95, 18.85, 24.66, 29.90]
df = pd.DataFrame({"Year": years, "Inflation Rate (%)": rates})

# --- Chart ---
st.subheader("Annual Inflation Trend")
fig = px.line(df, x="Year", y="Inflation Rate (%)", 
              markers=True, text="Inflation Rate (%)")
fig.update_traces(textposition="top center")
fig.update_layout(yaxis_title="Inflation Rate (%)")
st.plotly_chart(fig, use_container_width=True)

# --- Table ---
st.subheader("Historical Data")
st.dataframe(df, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Data Source: National Bureau of Statistics (NBS) | Portfolio Project")
