from ollama import chat
import streamlit as st 

input= st.text_input("Enter your question here..")
if input: 
    response = chat(
        model='gemma3:270m',
        # model='gemma3:1b',
        messages=[{'role': 'user', 'content': input}],
    )
    st.write(response.message.content)