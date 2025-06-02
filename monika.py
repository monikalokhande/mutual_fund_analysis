import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("mutual_funds_india.csv")
df.columns = df.columns.str.replace(" ", "")

# Display the title of the app
st.title("Mutual Fund Returns Dashboard")

# Display unique categories
st.subheader("Select a Category")
category = st.selectbox("Category", df.category.unique())

# Filter data based on category selected
filtered_data = df[df.category == category]

# Display unique AMCs for the selected category
st.subheader("Select an AMC Name")
amc_name = st.selectbox("AMC Name", filtered_data.AMC_name.unique())

# Filter data based on AMC selected
final_data = filtered_data[filtered_data.AMC_name == amc_name]

# Show a bar plot for mutual funds and their 1-year returns
st.subheader("1-Year Return of Mutual Funds")

# Create the barplot
plt.figure(figsize=[12,6])
sb.barplot(x=final_data.MutualFundName, y=final_data.return_1yr, palette='ocean')

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=90)

# Display the plot
st.pyplot(plt)

