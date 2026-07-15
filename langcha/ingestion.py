from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, DirectoryLoader 
from langchain_chroma import Chroma  # chromaDB
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

directory="db/chroma"

if not os.path.exists(directory):
    os.makedirs(directory)
    
doc_path='docs'

def load_documents(doc_path):
    if not os.path.exists(doc_path):
        raise FileNotFoundError("Documents directory not found")
    # text files
    text_loader= DirectoryLoader(doc_path,glob="*.txt", loader_cls=TextLoader, loader_kwargs={'encoding':'utf-8'})
    documents= text_loader.load()
    
    # pdf
    # pdf_loader= DirectoryLoader(doc_path,glob="*.pdf", loader_cls=PyPDFLoader)
    # pdf_docs= pdf_loader.load()
    
    # documents.extend(pdf_docs)
    
    if len(documents)==0:
        raise FileNotFoundError("No Documents found in directory")
    
    print(f"loaded documents- {len(documents)}")
    return documents


def chunk_documents(documents,chunk_size, chunk_overlap):
    splitter= RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks= splitter.split_documents(documents)
    
    if len(chunks)==0:
        raise ValueError("No Chunks Created")
    
    print(f"created chunks {len(chunks)}")
    return chunks
    
def create_vector(chunks, directory):
    embedder= OllamaEmbeddings(model="qwen3-embedding:0.6b")
    
    print("-----Creating Vector on the given path----")
    vectors= Chroma.from_documents(chunks, embedder, persist_directory=directory) 
    
    print("Vector Store Created Successfully")
    return vectors
    
if __name__=="__main__":
    d= load_documents(doc_path=doc_path)
    chunks= chunk_documents(d,chunk_size=800, chunk_overlap=100)
    vector= create_vector(chunks=chunks, directory=directory)
    
    