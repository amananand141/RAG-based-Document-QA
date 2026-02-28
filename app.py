# Connect all the Modular architecture --> Every module is indpt

import streamlit as st
from core.loader import load_pdfs
from core.splitter import split_documents
from core.embeddings import get_embeddings
from core.vectorstore import create_vector_store
from core.retriever import retrieve_docs
from core.qa import generate_answer

st.set_page_config(page_title="RAG Based Document QA", layout="wide") # wide layout better readability

st.title("📄Document Question Answering System")
st.write("Ask questions from you PDFs with source tracking 🔍")

# Session state init 
# so that DB should not get lost on every reload --- acts as a memory to vector DB
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# Upload PDFs -- Multiple file support 
uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files = True
)

# Process PDFs
if uploaded_files and st.button("Process Documents"): # button to process only when needed to rerun processing
    with st.spinner("Processing PDFs..."):
        docs = load_pdfs(uploaded_files)
        chunks = split_documents(docs)
        embeddings = get_embeddings()
        vectorstore = create_vector_store(chunks, embeddings)

        st.session_state.vectorstore = vectorstore

    st.success("Documents processed successfully!")

# Ask Question
if st.session_state.vectorstore: # Query selection--> wait till DB is ready
    query = st.text_input("Ask a question:")

    if query:
        with st.spinner("Thinking..."):
            docs = retrieve_docs(st.session_state.vectorstore, query)
            answer, sources, confidence = generate_answer(query, docs)

        st.subheader("🧠 Answer")   
        st.write(answer)

        st.subheader(f"📊 Confidence: {round(confidence * 100, 2)}%")

        st.subheader("📍 Sources")

        for src in sources:
            with st.expander(f"{src['file']} - Page {src['page']}"):
                st.write(src["snippet"])