import streamlit as st

option = st.selectbox(
    "Choose your skin type",
    ["Oily", "Dry", "Combination"]
)

st.write("You selected:", option)