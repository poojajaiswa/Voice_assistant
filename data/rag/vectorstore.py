from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings

def build_vector_store(docs):
    embeddings = OllamaEmbeddings(model="llama3")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
