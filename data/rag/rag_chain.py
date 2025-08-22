from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def get_rag_chain(vectorstore):
    llm = Ollama(model="llama3")  # Replaceable with llama3.1, llama3.2, etc.
    retriever = vectorstore.as_retriever()
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain
