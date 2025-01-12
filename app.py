import streamlit as st
import pandas as pd
import plotly.express as px
import nbformat


# Function to extract variables from the notebook
def execute_notebook(notebook_path):
    
    with open(notebook_path, "r") as f:
        notebook = nbformat.read(f, as_version=4)
    exec_env = {}
    for cell in notebook.cells:
        if cell.cell_type == "code":
            # Skip lines starting with `%` (Jupyter magic commands)
            code_lines = [
                line for line in cell.source.splitlines() if not line.strip().startswith("%")
            ]
            code_without_magics = "\n".join(code_lines)
            exec(code_without_magics, exec_env)
    return exec_env


# Load notebook
notebook_path = "Stock Analysis.ipynb"
variables = execute_notebook(notebook_path)

# Retrieve Plotly graph and DataFrame from notebook
dataframe1 = variables.get("stock1_revenue")
dataframe = variables.get("stock2_revenue")  # Replace 'your_dataframe' with the variable name from the notebook
plotly_graph = variables.get("fig")  # Replace 'your_plotly_graph' with the Plotly graph variable

# Streamlit app layout
st.title("Stock 2 revenue data")

# Display DataFrame
if dataframe is not None:
    st.subheader(variables.get("stock_2_ticker"))
    st.dataframe(dataframe)

# Display Plotly Graph
if plotly_graph is not None:
    st.subheader("Plotly Graph")
    st.plotly_chart(plotly_graph)
