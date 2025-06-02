import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# GitHub raw URL for the dataset (replace with your own URL)
url = "https://raw.githubusercontent.com/username/repository/branch/path/to/mutual_funds_india.csv"

# Try reading the CSV with error handling and different options
try:
    # Read CSV with a common delimiter (comma), encoding, and skip bad lines
    df = pd.read_csv(url, encoding='ISO-8859-1', sep=',', on_bad_lines='skip')  # Skip bad lines
    
    # Clean column names (remove spaces)
    df.columns = df.columns.str.strip()

    # Show column names to check if "category" exists
    st.write("Columns in the DataFrame:", df.columns)

    # Streamlit sidebar for category input (adjusted to reflect correct column name)
    category_column = 'category'  # Change this if the column name is different
    if category_column not in df.columns:
        st.error(f"Column '{category_column}' not found in the dataset. Please check the column names.")
    else:
        # Streamlit sidebar for category input
        st.sidebar.header("User Input")
        category = st.sidebar.selectbox("Select Category", df[category_column].unique())

        # Filter the data based on the selected category
        filtered_data = df[df[category_column] == category]

        # Streamlit sidebar for AMC selection
        amc_column = 'AMC_name'  # Change this if the column name is different
        if amc_column not in df.columns:
            st.error(f"Column '{amc_column}' not found in the dataset.")
        else:
            amc_name = st.sidebar.selectbox("Select AMC Name", filtered_data[amc_column].unique())

            # Filter data based on the selected AMC Name
            amc_filtered_data = filtered_data[filtered_data[amc_column] == amc_name]

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
