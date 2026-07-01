#pip install langchain langchain-core langchain-ollama 
from langchain_ollama import ChatOllama 
from langchain_core.prompts import ChatPromptTemplate 
import streamlit as st
llm= ChatOllama(
    model='gemma3:1b',
)
prompt= ChatPromptTemplate.from_template(
    "explain {topic} in simple language"
)

chain= prompt | llm 

st.header("langchain Ollama chat")

text= st.text_input('Enter Question here..')
if text:
    response= chain.invoke({
    'topic':{text}
    }) 
    st.write(response.content)