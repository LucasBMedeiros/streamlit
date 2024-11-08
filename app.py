# Libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Dashboard Title
st.title("Interactive Dashboard with Streamlit")

# Sample data for heatmap and table
np.random.seed(0)
data = np.random.rand(10, 5)
columns = [f"Metric {i}" for i in range(1, 6)]
df = pd.DataFrame(data, columns=columns)

## Charts
# Heatmap Section
st.header("Heatmap of Metrics")
fig, ax = plt.subplots()
sns.heatmap(df, annot=True, fmt=".2f", cmap="YlGnBu", ax=ax)
st.pyplot(fig)

# Table Section
st.header("Metrics Table")
st.dataframe(df)

## Sidebar, interactions
# Sidebar with Selectbox
st.sidebar.title("Controls")
metric_choice = st.sidebar.selectbox("Select Metric Column to Highlight", columns)

# Interactive Table Section
st.header("Interactive Metrics Table")
edited_df = st.data_editor(df, num_rows="dynamic") # allows editing and dynamic row addition

# Highlight selected column in the table
highlight = df.style.highlight_max(subset=[metric_choice], color='lightblue')
st.dataframe(highlight)
