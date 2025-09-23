import streamlit as st
import pandas as pd
import numpy as np

st.title("🚀 Streamlit in Docker")
st.write("This is a simple Streamlit app running inside a Docker container.")

# Input box
name = st.text_input("Enter your name:", "World")
st.write(f"Hello, {name}!")

# Example data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)
