from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# q="Langchain is the framework that is used in the Generative AI"
docs=[
    "Harjot is very good boy",
    "He is 22 years old",
    "he is the student of DAV university"
]
# model_embedding= OllamaEmbeddings(model="nomic-embed-text:latest")


# single query -> vector embedding

# ans= model_embedding.embed_query(q)
# print(f"Vector form of {q} is: {ans}")
# print(len(ans))

# ans= model_embedding.embed_documents(docs)
# print(f"Vector form of {docs} is: {ans}")
# print(len(ans))

# pip install langchain-text-splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter 

data=["Even though it started pouring rain right in the middle of our afternoon picnic, we quickly packed up all our food and decided to finish our lunch inside the cozy little coffee shop down the street",
"Because she wanted to make sure she was fully prepared for the upcoming job interview, she spent the entire weekend researching the company's history and practicing her answers to potential questions.",
"When we finally arrived at the bustling international airport after a long and exhausting drive, we realized we had accidentally left our passports sitting on the kitchen table back at the house.",
"Although the new Italian restaurant in the downtown district is a bit more expensive than the local diners, the incredible flavor of their handmade pasta is absolutely worth every single penny.",
"After the marathon race ended, the exhausted runners were grateful to receive medals, water bottles, and refreshing snacks at the finish line."]

splitter= RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=20)
# 0 to 50 - 1st chunk 
# 31 to 80 - 2nd chunk 

chunks=[]
for text in data:
    d= splitter.split_text(text)
    chunks.extend(d)

# print(chunks)
# print("--"*20)
# print("Length of chunks",len(chunks))

# print("Chunk-0", chunks[0])
# print("Chunk-1", chunks[1])

# vectors 
vector_chunks= model_embedding.embed_documents(chunks)
print(f"Length of vectors in per chunk: {len(vector_chunks[0])}")


for i, data in enumerate(vector_chunks):
    print("Vector-",i+1)
    print(data)
    # print(vector_chunks[i])


# print(len(ans))

