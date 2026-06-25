import streamlit as st 


# with st.form(key='myform'):
#     # col1, col2= st.columns(2)
#     col1, col2= st.columns([1,1])
#     with col1:
#         naam=st.text_input("Name",placeholder="Enter your name here...")
#         age= st.number_input("Age", min_value=5)    
#         password= st.text_input("Password",type='password')
#         gender= st.radio("Gender", options=['Male','Female'])
#     with col2:
#         city= st.selectbox("City",options=['Hoshiarpur','Jalandhar','Mohali','Chandigarh'],index=0)
#         marks= st.slider("Marks", min_value=10, max_value=30)
#         hobby= st.multiselect("Hobbies",options=['Gaming','Watching reels','Playing Cricket','Book reading'])
#     terms= st.checkbox("Terms and Conditions")
    
#     address= st.text_area("Address")
    
#     btn= st.form_submit_button("Save ")

#media tags 

# st.image('https://png.pngtree.com/thumb_back/fh260/background/20230411/pngtree-nature-forest-sun-ecology-image_2256183.jpg')

# st.video('https://youtu.be/YLoYcwnqVzM?si=yGQZeQfYotq4Ga7k')
# st.audio('')


# menu= st.selectbox("Menu",options=['Home','Contact','Blog'])
from streamlit_option_menu import option_menu
# pip install streamlit-option-menu
# menu= option_menu(menu_title="", options=['Home','Contact','Blog'],orientation='horizontal', icons=['house-fill','phone-fill','info'])

with st.sidebar:
    menu= option_menu(menu_title="", options=['Home','Contact','Blog'],orientation='vertical', icons=['house-fill','phone-fill','info'])

if menu=="Home":
    st.header("Home Page")
    st.sidebar.text_input("Name")
elif menu=="Contact":
    st.header("Contact Page")
elif menu=="Blog":
    st.header("Blog page")
    




