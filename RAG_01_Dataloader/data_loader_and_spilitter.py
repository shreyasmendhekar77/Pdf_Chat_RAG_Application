from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# apply text splitting and return the text_content list containing all docs

def split_text(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(data)
    text_content=[]
    for i in range(len(docs)):
        text_content.append(docs[i].page_content)

    return text_content
