import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Load Data from user_first_booking_cleaned.csv, df_response_138, and df_response_139
#Visualize bar chart of Total Users of Date Difference (0-30 days)
#Visualize response_hours distribution for user_segment_id 138
#Visualize response_hours distribution for user_segment_id 139

# Load Data
df_booking = pd.read_csv("user_first_booking_cleaned.csv")
df_response_138 = pd.read_csv("df_response_138.csv")
df_response_139 = pd.read_csv("df_response_139.csv")

st.title("User Activity Dashboard")

# Visualize var chart of Total Users of Date Difference (0-30 days)
st.header("Total Users by Date Difference (0-30 days)")
if "date_diff" in df_booking.columns:
    df_booking_filtered = df_booking[(df_booking["date_diff"] >= 0) & (df_booking["date_diff"] <= 30)]
    date_diff_counts = df_booking_filtered["date_diff"].value_counts().sort_index()
    fig1 = px.bar(
        x=date_diff_counts.index,
        y=date_diff_counts.values,
        labels={"x": "Date Difference (days)", "y": "Total Users"},
        title="Total Users by Date Difference (0-30 days)"
    )
    st.plotly_chart(fig1)
else:
    st.warning("Column 'date_diff' not found in user_first_booking_cleaned.csv.")

# Visualize response_hours distribution for user_segment_id 138
st.header("Response Hours Distribution for user_segment_id 138")
if "response_hours" in df_response_138.columns:
    fig2 = px.histogram(
        df_response_138,
        x="response_hours",
        nbins=30,
        title="Response Hours Distribution (Segment 138)"
    )
    st.plotly_chart(fig2)
else:
    st.warning("Column 'response_hours' not found in df_response_138.csv.")

# Visualize response_hours distribution for user_segment_id 139
st.header("Response Hours Distribution for user_segment_id 139")
if "response_hours" in df_response_139.columns:
    fig3 = px.histogram(
        df_response_139,
        x="response_hours",
        nbins=30,
        title="Response Hours Distribution (Segment 139)"
    )
    st.plotly_chart(fig3)
else:
    st.warning("Column 'response_hours' not found in df_response_139.csv.")