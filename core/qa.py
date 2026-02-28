from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer ONLY using the context below.
    If not found, say "Answer not found in document."

    Context:
    {context}

    Question: {query}
    """

    response = client.models.generate_content(
        model="models/gemini-flash-latest",  # 🔥 FINAL FIX
        contents=prompt
    )

    answer = response.text

    sources = []
    for doc in docs:
        sources.append({
            "file": doc.metadata.get("source"),
            "page": doc.metadata.get("page"),
            "snippet": doc.page_content[:150]
        })

    confidence = min(len(docs) / 3, 1.0)

    return answer, sources, confidence