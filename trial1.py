
        
        
     

    
import streamlit as st

st.title("🌟Know Your Cure")
st.image("https://raw.githubusercontent.com/Yatharth-Vasu/trial-1/main/webapp.png.png" , width = 150)
product = []
while st.button('end'):
    product = st.text_input("Enter product name")
n3 = []
n3.append(product)
if st.button("Done"):
   st.write(n3)


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
   
    elif(n1 == 'Oily' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. The Derma Co Pore Minimizing Toner – 
https://thedermaco.com/products/2-niacinamide-pore-minimizing-face-toner
                 
2. COSRX AHA/BHA Clarifying Treatment Toner – 
https://www.cosrx.com/products/aha-bha-clarifying-treatment-toner
                 
3. Dot & Key Rice Water Hydrating Toner – 
https://www.dotandkey.com/products/rice-water-probiotics-hydrating-toner""")
    elif(n1 == 'Oily' and n2 == '🔬Serum'):
        st.write("""🔬Serum :
                 
1. Minimalist Niacinamide 5% Serum – 
https://beminimalist.co/products/niacinamide-5-serum
                 
2. The Ordinary Niacinamide 10% + Zinc 1% – 
https://theordinary.com/en-us/niacinamide-10-zinc-1-serum
                 
3. The Derma Co Niacinamide Serum – 
https://thedermaco.com/products/10-niacinamide-face-serum""")
    elif(n1 == 'Oily' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Deconstruct Gel Sunscreen SPF 55 – 
https://thedeconstruct.in/products/gel-sunscreen-spf-55-pa
                 
2. Fixderma Shadow SPF 50+ Gel – 
https://www.fixderma.com/products/shadow-spf-50-gel
                 
3. Beauty of Joseon Relief Sun SPF 50+ – 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics""")
    elif(n1 == "Oily" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
1. Pond's Super Light Gel – 
https://www.ponds.com/in/p/super-light-gel.html
                 
2. Minimalist Vitamin B5 10% Moisturizer – 
https://beminimalist.co/products/vitamin-b5-10-moisturizer
                 
3. Re'equil Oil Free Moisturiser – 
https://www.reequil.com/products/oil-free-moisturiser""")
    elif(n1 == "Dry" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :

1. Cetaphil Gentle Skin Cleanser – 
https://www.cetaphil.com/us/cleansers/gentle-skin-cleanser
                 
2. CeraVe Hydrating Cleanser – 
https://www.cerave.com/skincare/cleansers/hydrating-facial-cleanser
                 
3. Bioderma Atoderm Gel Moussant –
https://www.bioderma.us/all-products/atoderm/shower-gel""")
    elif(n1 == 'Dry' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Klairs Supple Preparation Facial Toner – 
https://www.klairscosmetics.com/product/supple-preparation-facial-toner/
                 
2. Laneige Cream Skin Refiner – 
https://www.laneige.com/int/en/skincare/cream-skin.html
                 
3. TONYMOLY Wonder Ceramide Mochi Toner – 
https://tonymoly.us/products/wonder-ceramide-mochi-toner""")
    elif(n1 == 'Dry' and n2 == '🔬Serum'):
        st.write("""🔬Serum :
                 
1. L'Oréal Paris Hyaluronic Acid Serum – 
 https://www.lorealparis.co.in/revitalift/revitalift-1-5-percent-hyaluronic-acid-serum
                 
2. Minimalist Hyaluronic Acid 2% Serum – 
 https://beminimalist.co/products/hyaluronic-acid-2-percent-serum
                 
3. The Ordinary Hyaluronic Acid 2% + B5 – 
https://theordinary.com/en-us/hyaluronic-acid-2-b5-serum""")
    elif(n1 == 'Dry' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Beauty of Joseon Relief Sun SPF 50+ – 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics
                 
2. Isntree Hyaluronic Acid Watery Sun Gel – 
https://en.isntree.com/products/hyaluronic-acid-watery-sun-gel
                 
3. Neutrogena Ultra Sheer SPF 50 – 
https://www.neutrogena.com/products/sun/ultra-sheer-dry-touch-sunscreen-broad-spectrum-spf-50""")
    elif(n1 == "Dry" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. CeraVe Moisturizing Cream – 
https://www.cerave.com/skincare/moisturizers/moisturizing-cream
                 
2. Cetaphil Moisturising Cream – 
https://www.cetaphil.com/us/moisturizers/moisturizing-cream
                 
3. Bioderma Atoderm Crème – 
https://www.bioderma.us/all-products/atoderm/cream""")
    elif(n1 == "Normal" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Cetaphil Gentle Skin Cleanser – 
https://www.cetaphil.com/us/cleansers/gentle-skin-cleanser
                 
2. CeraVe Hydrating Cleanser – 
https://www.cerave.com/skincare/cleansers/hydrating-facial-cleanser""")
    elif(n1 == 'Normal' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Klairs Supple Preparation Unscented Toner – 
https://www.klairscosmetics.com/product/supple-preparation-unscented-toner/
                 
2. Dot & Key Rice Water Toner – 
https://www.dotandkey.com/products/rice-water-probiotics-hydrating-toner""")
    elif(n1 == 'Normal' and n2 == '🔬Serum'):
        st.write("""🔬Serum : 
                 
1. Minimalist Vitamin C 10% Serum – 
https://beminimalist.co/products/vitamin-c-10-face-serum
                 
2. L'Oréal Paris Revitalift Hyaluronic Acid Serum – 
https://www.lorealparis.co.in/revitalift/revitalift-1-5-percent-hyaluronic-acid-serum
                 
3. Plum Vitamin C Serum – 
https://plumgoodness.com/products/15-vitamin-c-face-serum""")
    elif(n1 == 'Normal' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Minimalist Light Fluid Sunscreen SPF 50 – 
https://beminimalist.co/products/light-fluid-spf-50-sunscreen
                 
2. Beauty of Joseon Relief Sun SPF 50+ – 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics""")
    elif(n1 == "Normal" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Cetaphil Moisturising Lotion – 
https://www.cetaphil.com/us/moisturizers/moisturizing-lotion
                 
2. Neutrogena Hydro Boost Water Gel – 
https://www.neutrogena.com/products/skincare/hydro-boost-water-gel
                 
3. Simple Hydrating Light Moisturiser – 
https://www.simpleskincare.in/products/hydrating-light-moisturiser""")
    elif(n1 == "Combination" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Simple Refreshing Face Wash – 
https://www.simpleskincare.in/products/kind-to-skin-refreshing-facial-wash
                 
2. Cetaphil Oily Skin Cleanser – 
https://www.cetaphil.com/us/cleansers/oily-skin-cleanser""")
    elif(n1 == 'Combination' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Dot & Key Rice Water Toner – 
https://www.dotandkey.com/products/rice-water-probiotics-hydrating-toner
                 
2. Simple Soothing Facial Toner – 
https://www.simpleskincare.in/products/kind-to-skin-soothing-facial-toner""")
    elif(n1 == 'Combination' and n2 == '🔬Serum'):
        st.write("""🔬Serum : 
                 
1. Minimalist Niacinamide 5% Serum – 
https://beminimalist.co/products/niacinamide-5-serum
                 
2. Minimalist Vitamin C 10% Serum – 
https://beminimalist.co/products/vitamin-c-10-face-serum""")
    elif(n1 == 'Combination' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
1. Minimalist Light Fluid Sunscreen SPF 50 – 
https://beminimalist.co/products/light-fluid-spf-50-sunscreen
                 
2. Deconstruct Gel Sunscreen SPF 55 – 
https://thedeconstruct.in/products/gel-sunscreen-spf-55-pa""")
    elif(n1 == "Combination" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Neutrogena Hydro Boost Water Gel – 
https://www.neutrogena.com/products/skincare/hydro-boost-water-gel
                 
2. Simple Hydrating Light Moisturiser – 
https://www.simpleskincare.in/products/hydrating-light-moisturiser""")
    elif(n1 == "Sensitive" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Cetaphil Gentle Skin Cleanser – 
https://www.cetaphil.com/us/cleansers/gentle-skin-cleanser
                 
2. CeraVe Hydrating Cleanser – 
https://www.cerave.com/skincare/cleansers/hydrating-facial-cleanser
                 
3. Physiogel Daily Moisture Therapy Cleanser – 
https://www.physiogel.com/products/daily-moisture-therapy-cleanser""")
    elif(n1 == 'Sensitive' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Klairs Supple Preparation Unscented Toner – 
https://www.klairscosmetics.com/product/supple-preparation-unscented-toner/
                 
2. Pyunkang Yul Essence Toner – 
https://pyunkangyul.us/products/essence-toner
                 
3. Simple Soothing Facial Toner – 
https://www.simpleskincare.in/products/kind-to-skin-soothing-facial-toner""")
    elif(n1 == 'Sensitive' and n2 == '🔬serum'):
        st.write("""🔬Serum :
                 
1. Minimalist Sepicalm 3% Serum – 
https://beminimalist.co/products/sepicalm-3-oat-serum
                 
2. The Ordinary Soothing & Barrier Support Serum – 
https://theordinary.com/en-us/soothing-barrier-support-serum
                 
3. Purito Centella Unscented Serum – 
https://purito.com/product/centella-unscented-serum/""")
    elif(n1 == 'Sensitive' and n2 == '☀️sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. La Roche-Posay Anthelios SPF 50+ – 
https://www.laroche-posay.com/anthelios
                 
2. Beauty of Joseon Relief Sun SPF 50+ – 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics
                 
3. Bioderma Photoderm Max SPF 50+ – 
https://www.bioderma.us/all-products/photoderm/max-spf-50""")
    elif(n1 == "Sensitive" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Physiogel Daily Moisture Therapy Cream – 
https://www.physiogel.com/products/daily-moisture-therapy-cream
                 
2. CeraVe Moisturizing Cream – 
https://www.cerave.com/skincare/moisturizers/moisturizing-cream
                 
3. Aveeno Daily Moisturizing Lotion – 
https://www.aveeno.com/products/daily-moisturizing-lotion""")
    elif(n1 == "Delusional Korean Glass SKin😂😂😂" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Beauty of Joseon Green Plum Refreshing Cleanser – 
https://beautyofjoseon.com/products/green-plum-refreshing-cleanser
                 
2. COSRX Low pH Good Morning Gel Cleanser – 
https://www.cosrx.com/products/low-ph-good-morning-gel-cleanser
                 
3. Round Lab 1025 Dokdo Cleanser – 
https://roundlab.com/products/1025-dokdo-cleanser""")
    elif(n1 == 'Delusional Korean Glass SKin😂😂😂' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Anua Heartleaf 77% Soothing Toner – 
https://anua.kr/products/heartleaf-77-soothing-toner
                 
2. Round Lab 1025 Dokdo Toner – 
https://roundlab.com/products/1025-dokdo-toner
                 
3. TIRTIR Milk Skin Toner – 
https://tirtir.global/products/milk-skin-toner""")
    elif(n1 == 'Delusional Korean Glass SKin😂😂😂' and n2 == '🔬Serum'):
        st.write("""🔬Serum :
                 
1. Beauty of Joseon Glow Serum (Propolis + Niacinamide) – 
https://beautyofjoseon.com/products/glow-serum-propolis-niacinamide
                 
2. Beauty of Joseon Glow Deep Serum (Rice + Alpha-Arbutin) – 
https://beautyofjoseon.com/products/glow-deep-serum-rice-arbutin
                 
3. Anua Niacinamide 10% + TXA 4% Serum – 
https://anua.kr/products/niacinamide-10-txa-4-serum""")
    elif(n1 == 'Delusional Korean Glass SKin😂😂😂' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Beauty of Joseon Relief Sun SPF50+ PA++++ – 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics
                 
2. Round Lab Birch Juice Moisturizing Sun Cream SPF50+ – 
https://roundlab.com/products/birch-juice-moisturizing-sun-cream
                 
3. Isntree Hyaluronic Acid Watery Sun Gel SPF50+ – 
https://en.isntree.com/products/hyaluronic-acid-watery-sun-gel""")
    elif(n1 == "Delusional Korean Glass SKin😂😂😂" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Beauty of Joseon Dynasty Cream – 
https://beautyofjoseon.com/products/dynasty-cream
                 
2.COSRX Advanced Snail 92 All In One Cream – 
https://www.cosrx.com/products/advanced-snail-92-all-in-one-cream
                 
3.Round Lab Birch Juice Moisturizing Cream – 
https://roundlab.com/products/birch-juice-moisturizing-cream""")
