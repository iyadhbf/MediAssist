from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents: list) -> list:
    """
    Splits documents into overlapping chunks for better retrieval.
    chunk_size=500, overlap=100 is optimal for medical short fiches.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["===", "\n\n", "\n", " "]  # respects our fiche structure
    )

    chunks = splitter.split_documents(documents)
    print(f"✅ Created {len(chunks)} chunks")
    return chunks