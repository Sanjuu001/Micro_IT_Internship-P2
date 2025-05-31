import streamlit as st
from calculator import calculate

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.markdown("Perform basic arithmetic operations easily!")

# Input fields
num1 = st.text_input("Enter the first number", value="0")
num2 = st.text_input("Enter the second number", value="0")

operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate button
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")