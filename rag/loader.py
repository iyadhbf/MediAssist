from langchain_community.document_loaders import TextLoader, PyPDFLoader
from pathlib import Path

def load_documents(data_dir: str = "data") -> list:
    """
    Loads all .txt and .pdf files from the data directory.
    Returns a list of LangChain Document objects.
    """
    documents = []
    data_path = Path(data_dir)

    for file in data_path.iterdir():
        if file.suffix == ".txt":
            loader = TextLoader(str(file), encoding="utf-8")
            documents.extend(loader.load())
        elif file.suffix == ".pdf":
            loader = PyPDFLoader(str(file))
            documents.extend(loader.load())

    print(f"✅ Loaded {len(documents)} document(s) from {data_dir}/")
    return documents