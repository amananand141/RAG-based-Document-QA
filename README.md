# 📄 RAG-Based Document QA System (Gemini Powered)

A Retrieval-Augmented Generation (RAG) system that allows users to query PDF documents and get accurate, source-backed answers using Google Gemini.

## ❓ Problem

Large Language Models (LLMs):
- ❌ Hallucinate answers  
- ❌ Cannot access private documents  
- ❌ Do not provide source transparency  

---

## ✅ Solution

This project implements a **RAG (Retrieval-Augmented Generation)** system that:

- Retrieves relevant chunks from PDF documents  
- Uses **Gemini LLM** to generate grounded answers  
- Provides **source references (file + page + snippet)**  

---

## 🚀 Features

- 📂 Upload multiple PDFs  
- 🔍 Semantic search using FAISS  
- 🤖 Gemini-powered answers  
- 📍 Source tracking (file + page + snippet)  
- 📊 Confidence score  
- ⚡ Fast and interactive UI (Streamlit)  
- 🧩 Modular architecture (easy to extend)

---

## 🏗️ Architecture


PDF Documents
↓
Document Loader
↓
Text Splitter (Chunking)
↓
Embeddings (HuggingFace)
↓
FAISS Vector Store
↓
Retriever (Top-K Chunks)
↓
Gemini LLM
↓
Answer + Sources + Confidence


---

## 📸 Demo

![Demo](assets/demo.png)

---

## ⚙️ Tech Stack

| Component        | Technology |
|----------------|-----------|
| Frontend       | Streamlit |
| Backend        | Python |
| LLM            | Google Gemini API |
| Embeddings     | HuggingFace (all-MiniLM-L6-v2) |
| Vector DB      | FAISS |
| Framework      | LangChain |

---

## 📁 Project Structure


rag-document-qa/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── core/
│ ├── loader.py
│ ├── splitter.py
│ ├── embeddings.py
│ ├── vectorstore.py
│ ├── retriever.py
│ └── qa.py


---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/amananand141/RAG-based-Document-QA.git
cd RAG-based-Document-QA

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Setup environment variables

Create a .env file:

GOOGLE_API_KEY=your_api_key_here

5. Run the app
streamlit run app.py
