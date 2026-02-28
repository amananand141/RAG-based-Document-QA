def retrieve_docs(vectorstore, query, k=3):
    """
    Retrieve top-k relevant documents from vector store.

    Args:
        vectorstore: FAISS vector DB
        query: user question
        k: number of top results

    Returns:
        List of relevant Document objects
    """

    docs = vectorstore.similarity_search(query, k=k) # FAISS find nearest vectors then it selects top k chunks

    return docs # returns original document objects so that we can keep the track of source and page no.