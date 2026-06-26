import streamlit as st

st.title("Know Your Cure")
st.image("https://raw.githubusercontent.com/Yatharth-Vasu/trial-1/main/webapp.png.png" , width = 150)
n1 = st.selectbox(
    "Choose your skin type",
    ["Oily"]
)


n2 = st.selectbox("which product do u want" , ["Face wash"])
if st.button("Identify Cure"):

    if( n1 == "Oily" and n2 == "Face wash"  ):
        st.write("""Oily & Acne-Prone Skin:
 *Face Wash* -
 
1. The Derma Co 1% Salicylic Acid Gel Face Wash – """)
st.link_button("Buy Now", "https://thedermaco.com/product/1-salicylic-acid-gel-face-wash-the-dermaco-100ml/")


