import streamlit as st
n1 = st.selectbox(
    "Choose your skin type",
    ["Oily", "Dry", "Combination"]
)
st.title("Know Your Cure")

n2 = st.selectbox("which product do u want" , ["Face wash" , "Toner"])
if st.button("Identify Cure"):

    if( n1 == "Oily" and n2 == "Face wash"  ):
        st.write("""Oily & Acne-Prone Skin:
 *Face Wash* -
1. The Derma Co 1% Salicylic Acid Gel Face Wash
2. Minimalist 2% Salicylic Acid Cleanser
3. Chemist At Play Oil & Acne Control Face Wash
 *Toner* -
1. The Derma Co Pore Minimizing Toner
2. COSRX AHA/BHA Clarifying Treatment Toner
3. Dot & Key Rice Water Toner
 *Serum* -
1. Minimalist Niacinamide 5% Serum
2. The Ordinary Niacinamide 10% + Zinc 1%
3. The Derma Co Niacinamide Serum
 *Moisturizer* -
1. Pond's Super Light Gel
2. Minimalist Vitamin B5 10% Moisturizer
3. Re'equil Oil Free Moisturiser
 *Sunscreen* -
1. Deconstruct Gel Sunscreen SPF 55
2. Fixderma Shadow SPF 50+ Gel
3. Beauty of Joseon Relief Sun SPF 50+""")
    
