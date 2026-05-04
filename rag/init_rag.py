from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.vectorstore import build_vectorstore

if __name__ == "__main__":
    print("🔄 Initializing RAG pipeline...")
    docs = load_documents("data")
    chunks = chunk_documents(docs)
    build_vectorstore(chunks)
    print("🎉 RAG pipeline ready!")