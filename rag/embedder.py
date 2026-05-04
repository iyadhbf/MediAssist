from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",  # ✅ only ~90MB, very fast
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    print("✅ Embedding model loaded")
    return embeddings