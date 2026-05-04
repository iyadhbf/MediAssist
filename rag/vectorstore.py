from langchain_chroma import Chroma
from rag.embedder import get_embeddings

CHROMA_DIR = "./chroma_db"

def build_vectorstore(chunks: list) -> Chroma:
    """Embeds chunks and stores them in ChromaDB."""
    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )
    print(f"✅ Vectorstore built with {len(chunks)} chunks")
    return vectorstore


def load_vectorstore() -> Chroma:
    """Loads an existing ChromaDB vectorstore from disk."""
    embeddings = get_embeddings()
    vectorstore = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )
    print("✅ Vectorstore loaded from disk")
    return vectorstore