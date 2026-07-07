from langchain_ollama import ChatOllama
from langchain_classic.memory import ConversationBufferMemory,ConversationSummaryMemory, ConversationTokenBufferMemory 
from langchain_classic.chains import ConversationChain 

llm= ChatOllama(model='gemma3:1b')

# memory = ConversationBufferMemory()
memory = ConversationSummaryMemory(llm=llm)
# memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=100)
chatbot= ConversationChain(llm=llm, memory=memory, verbose=False) # True- shows internal execuation 

while True:
    user=input("You: ")
    if user.lower()=="exit":
        print("Memory:",memory.load_memory_variables({}))
        break 
    response= chatbot.predict(input=user)
    print("AI:",response)
