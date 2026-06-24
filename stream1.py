# pip install streamlit 
# to run - streamlit run stream1.py
# or python -m streamlit run file_name.py
import streamlit as st 

st.set_page_config(page_title='Home Page', page_icon='🏠')

st.header("Python langchain")
st.subheader("Python Subheading")

st.write("Streamlit is an open-source Python library that allows developers, data scientists, and AI engineers to build interactive, shareable web applications using only pure Python. It completely eliminates the need to write HTML, CSS, JavaScript, or handle backend routing")

# naam= st.text_input('Name')
# # btn = st.button("Submit")

# # if st.button("Submit"): 
# #     st.write(naam)
# #     st.balloons()
# if naam: 
#     st.write(naam)
#     st.balloons()

with st.form(key='myform'):
    naam=st.text_input("Name",placeholder="Enter your name here...")
    age= st.number_input("Age", min_value=5)    
    password= st.text_input("Password",type='password')
    gender= st.radio("Gender", options=['Male','Female'])
    terms= st.checkbox("Terms and Conditions")
    address= st.text_area("Address")
    city= st.selectbox("City",options=['Hoshiarpur','Jalandhar','Mohali','Chandigarh'],index=0)
    hobby= st.multiselect("Hobbies",options=['Gaming','Watching reels','Playing Cricket','Book reading'])
    
    btn= st.form_submit_button("Save ")