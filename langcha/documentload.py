# document loaders -
# text files, csv, pdf, directory loader

from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, DirectoryLoader

# loader= TextLoader('docs/name.txt')
# documents= loader.load()
# print(documents)
# # print(documents[0])
# print(documents[0].page_content)


# pdf load 

pdf=PyPDFLoader('docs/attention-is-all-you-need.pdf')
pdf_docs= pdf.load()

# print(pdf_docs)

# for i, page in enumerate(pdf_docs):
#     print(f"Document {i+1},Source:{page.metadata}, Page content length: {len(page.page_content)}")
    
    
# csv loader 
# csv= CSVLoader('docs/used_cars_data.csv')
# csv_data= csv.load()
# print(csv_data)
# print(len(csv_data))


#directory loader 
dloader= DirectoryLoader("docs",glob="*.txt", loader_cls=TextLoader, loader_kwargs={'encoding':'utf-8'})
documents=dloader.load()

print(documents)
print("Total number of documents loaded",len(documents))

for doc in documents:
    print(doc.metadata['source'])
    print(doc.page_content[:50])
    print("*"*20)