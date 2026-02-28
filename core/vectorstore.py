from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embeddings):#chunks-> splitter o/p #embeddings-> embedding model
    # creates vector index
    # Attach metadata
    # Build searchable database
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore