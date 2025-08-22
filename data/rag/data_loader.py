from langchain_community.document_loaders import TextLoader, CSVLoader

def load_data(file_path: str):
    if file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    elif file_path.endswith(".csv"):
        loader = CSVLoader(file_path)
    else:
        raise ValueError("Unsupported file format. Use .txt or .csv")
    
    return loader.load()
