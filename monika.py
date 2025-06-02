import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# GitHub raw URL for the dataset (replace with your own URL)
url = "https://github.com/monikalokhande/mutual_fund_analysis/blob/main/mutual_funds_india.csv"

# Try reading the CSV with error handling and different options
try:
    # Test reading with a common delimiter (comma), encoding, and skip bad lines
    df = pd.read_csv(url, encoding='ISO-8859-1', sep=',', on_bad_lines='skip')  # Skip bad lines
    st.write("CSV Loaded successfully!")

    # Clean column names (remove spaces)
    df.columns = df.columns.str.replace(" ", "")

    # Streamlit sidebar for category input
    st.sidebar.header("User Input")
    category = st.sidebar.selectbox("Select Category", df.category.unique())

    # Filter the data based on the selected category
    filtered_data = df[df.category == category]

    # Streamlit sidebar for AMC selection
    amc_name = st.sidebar.selectbox("Select AMC Name", filtered_data.AMC_name.unique())

    # Filter data based on the selected AMC Name
    amc_filtered_data = filtered_data[filtered_data.AMC_name == amc_name]

    # Show a table of selected Mutual Funds
    st.write(f"### Mutual Funds under '{category}' and '{amc_name}'")
    st.dataframe(amc_filtered_data[['MutualFundName', 'return_1yr']])

    # Plot the 1-year return for mutual funds
    st.write(f"### 1-Year Return for Mutual Funds in {amc_name}")
    plt.figure(figsize=[12, 6])
    sb.barplot(x=amc_filtered_data.MutualFundName, y=amc_filtered_data.return_1yr, palette='ocean')
    plt.xticks(rotation=90)
    st.pyplot(plt)

except pd.errors.ParserError as e:
    st.error(f"Error reading the CSV file: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")
