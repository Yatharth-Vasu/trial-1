import streamlit as st

st.title("🌟Know Your Cure")
st.image("https://raw.githubusercontent.com/Yatharth-Vasu/trial-1/main/webapp.png.png" , width = 150)
n3 = []
n3.append(input())
if st.button("Done"):
   print(n3)

n1 = st.selectbox(
    "Choose your skin type",
    ["Oily" ,  "Dry" , "Normal" , "Combination" , "Sensitive" , "Delusional Korean Glass SKin😂😂😂"]
)


n2 = st.selectbox("which product do u want" , ["🧼Face wash" , "💧Toner" , "🔬Serum" , "☀️Sunscreen" , "🧴Moisturizer"])
        if st.button("Identify Cure"):

            if( n1 == "Oily" and n2 == "🧼Face wash"  ):
                st.write("""🧼Face Wash :
 
1. The Derma Co 1% Salicylic Acid Gel Face Wash –
 https://thedermaco.com/product/1-salicylic-acid-gel-face-wash-the-dermaco-100ml/

2.Minimalist 2% Salicylic Acid + LHA Cleanser – 
https://beminimalist.co/products/salicylic-lha-2-cleanser

3.Chemist At Play Oil & Acne Control Face Wash – 
https://innovist.com/products/oil-acne-control-face-wash """)
   
        

        
        
     

    
