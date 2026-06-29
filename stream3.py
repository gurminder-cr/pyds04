import streamlit as st 
import base64 

st.set_page_config("BG Image")

with open('img.jpg','rb') as f:
    image= f.read()

img= base64.b64encode(image).decode()

# data-testid="stAppViewContainer" 
st.button("Save Details")
css =f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background-image:url(data:image/png;base64,{img});
        background-size: cover
    }}
    [data-testid="stHeader"]{{
        background-color:#8c7c51;
        color:white
    }}
    [data-testid="stBaseButton-secondary"]{{
        background-color:red;
        color:white
    }}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)