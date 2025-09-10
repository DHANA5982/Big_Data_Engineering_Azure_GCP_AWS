import streamlit as st

st.set_page_config(page_title="Welcome Page", page_icon="👋", layout="centered")

st.title("👋 Welcome to Streamlit in Docker!")
st.write("""
This is a simple **Streamlit app** running inside a **Docker container**.  
You can use this setup to test, learn, and deploy your Python apps easily.
""")

name = st.text_input("Enter your name:", "")
if name:
    st.success(f"Hello, {name}! 🎉 Welcome to Docker + Streamlit Web Interface.")
    