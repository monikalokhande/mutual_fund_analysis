import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import os

# Load the dataset (make sure to provide the correct path)
dataset_path = "mutual_funds_india.csv"

# Check if the file exists
if not os.path.exists(dataset_path):
    st.error(f"Dataset file not found at {dataset_path}")
else:
    # Read the CSV file
    df = pd.read_csv(dataset_path)

    # Clean up the column names by removing spaces
    df.columns = df.columns.str.replace(" ", "")

    # Display the title of the app
    st.title("Mutual Fund Returns Dashboard")

    # Show a brief description of the app
    st.write("""
        This app allows you to explore the 1-year returns of mutual funds based on selected categories and AMC names.
    """)

    # Step 1: Select Category
    st.subheader("Select a Category")
    category = st.selectbox("Category", df.category.unique())

    # Step 2: Filter data by the selected category
    filtered_data = df[df.category == category]

    # Step 3: Select AMC Name based on the selected category
    st.subheader("Select an AMC Name")
    amc_name = st.selectbox("AMC Name", filtered_data.AMC_name.unique())

    # Step 4: Filter data by the selected AMC
    final_data = filtered_data[filtered_data.AMC_name == amc_name]

    # Display a preview of the filtered data
    st.write("### Data Preview", final_data.head())

    # Step 5: Create a Bar Plot for 1-Year Return
    st.subheader("1-Year Return of Mutual Funds")

    # Create the barplot using seaborn
    plt.figure(figsize=[12,6])
    sb.barplot(x=final_data.MutualFundName, y=final_data.return_1yr, palette='ocean')

    # Rotate x-axis labels to avoid overlap
    plt.xticks(rotation=90)

    # Display the plot in Streamlit
    st.pyplot(plt)

    # Optionally, save the plot as an image
    save_plot = st.checkbox("Save Plot as Image")
    if save_plot:
        save_path = os.path.join(os.getcwd(), "1_year_returns_plot.png")
        plt.savefig(save_path)
        st.success(f"Plot saved at: {save_path}")

