# basic_app.py

import streamlit as st

# 1. Set the Title
st.title("Bear's Site")
st.subheader("Bears are often in their cave.")

# 2. Add a Text Input Widget
user_name = st.text_input("Enter your name:", "Bear")

# 3. Add a Slider Widget
slider_value = st.slider("Select a number:", 0, 100, 25)

# 4. Display the Output
st.write(f"Hello, **{user_name}**! Your selected number is **{slider_value}**.")

# 5. Add a simple data display (using a dictionary)
st.write("### Bear's favorite ice cream")
st.code("Something with coffee")