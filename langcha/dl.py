# document loading 

from langchain_community.document_loaders import PyPDFLoader ,TextLoader,CSVLoader ,DirectoryLoader

# loader=TextLoader('docs/name.txt')

# documents=loader.load()

# print(documents)

# print(documents[0].page_content)

# print(documents[0].metadata)


pdfloader=PyPDFLoader('docs/attention-is-all-you-need.pdf')

pdf_doc=pdfloader.load()



for i,page in enumerate(pdf_doc):
    print(f"Document {i+1}, Source: {page.metadata} ,Page content lenght: {len(page.page_content)}")


# CSV File loader 

# csv=CSVLoader('Housing.csv')

# csvdata=csv.load()

# print(len(csvdata))

# print(csvdata[0].page_content)


# path="docs"
# loader=DirectoryLoader(path,glob="*.txt",loader_cls=TextLoader,loader_kwargs={'encoding':'utf-8'})

# documents=loader.load()

# pdf_loader=DirectoryLoader(path,glob="*.pdf",loader_cls=PyPDFLoader)

# pdfdoc=pdf_loader.load()

# documents.extend(pdfdoc)


# csv_loader=DirectoryLoader(path,glob="*.csv",loader_cls=CSVLoader)
# csvdocs=csv_loader.load()

# documents.extend(csvdocs)

# print(f"Total Number of documents loaded :{len(documents)} ")

# for doc in documents:
#     print(doc.metadata["source"])
#     print(doc.page_content[:100])
#     print("*"*100)