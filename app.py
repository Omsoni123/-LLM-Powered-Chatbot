import streamlit as st
import pinecone
from sentence_transformers import SentenceTransformer

# Initialize Pinecone
INDEX_NAME = "llmmodel"  

pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# Load sentence transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Streamlit UI
st.title("🔍 LLM-Powered Chatbot")
st.write("Ask questions based on the indexed documents.")

user_query = st.text_input("Enter your query:")

if user_query:
    query_embedding = model.encode(user_query).tolist()
    search_results = index.query(vector=query_embedding, top_k=1, include_metadata=True)

    st.subheader("Results:")
    for match in search_results["matches"]:
        st.write(f"📌 **{match['metadata']['text']}**")
