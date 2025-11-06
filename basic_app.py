# basic_app.py

import streamlit as st

# 1. Set the Title
st.title("My First Streamlit App 🎈")
st.subheader("Interactive Widgets Demo")

# 2. Add a Text Input Widget
user_name = st.text_input("Enter your name:", "World")

# 3. Add a Slider Widget
slider_value = st.slider("Select a number:", 0, 100, 25)

# 4. Display the Output
st.write(f"Hello, **{user_name}**! Your selected number is **{slider_value}**.")

# 5. Add a simple data display (using a dictionary)
st.write("### Data Display")
st.code("This is how you display code or formulas.")