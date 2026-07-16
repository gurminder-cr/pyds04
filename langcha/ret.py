from langchain_chroma import Chroma 
from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# vector database 
PERSIST_DIRECT="db/chroma"

embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        encode_kwargs={"normalize_embeddings": True}
    )
vector_store= Chroma(persist_directory=PERSIST_DIRECT, embedding_function=embeddings)

retriever= vector_store.as_retriever(
    search_kwargs={'k':5}
)

# function - context 
def format_docs(docs):
    return "\n".join(doc.page_content for doc in docs)

prompt= ChatPromptTemplate.from_template("""
    You are helpful AI Assistant.
    Answer Only using the provided Context.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Strict Rules:
    1. Do not answer anything outside the context.
    2. If the answer is not present in the context reply"I Do not have any context about the question you have asked"
                                         
    Answer:                                       
""")

# llm
llm= ChatOllama(
    # model='llama3.2:1b'
    model='gemma3:latest'
    )

# LCEL Chain 

chain=(
    {
        'context':retriever | format_docs,
        'question':RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)
while True:
    question=input("You: ")
    if question.lower()=='exit':
        break 
    answer= chain.invoke(question)
    print("----\n Answer \n------")
    print(answer)