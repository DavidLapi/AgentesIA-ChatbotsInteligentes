import streamlit as st
import faiss
import numpy as np
import pypdf
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

# Load AI Model
llm = OllamaLLM(model="mistral") # Change to "llama3" or another Ollama model

# Load Hugging Face Embeddings 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize FAISS Vector Database
index = faiss.IndexFlatL2(384) # Vector dimension for MiniLM
vector_store = {}

# Function to extract text from PDFs
def extract_text_from_pdf(uploaded_file): #1
    pdf_reader = pypdf.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to store text in FAISS
def store_in_faiss(text, filename):
    global index, vector_store
    st.write(f"📩 Storing document '{filename}' in FAISS...")

    # Split text into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_text(text)

    # Convert text into embeddings
    vectors = embeddings.embed_documents(texts)
    vectors = np.array(vectors, dtype=np.float32)

    # Store in FAISS
    index.add(vectors)
    vector_store[len(vector_store)] = (filename, texts)
    
    return "✅ Document stored successfully!"

# Function to retrieve relevant chunks and answer questions
def retrieve_and_answer(query):
    global index, vector_store

    # Convert query into embeddings
    query_vector = np.array(embeddings.embed_query(query), dtype=np.float32).reshape(1, -1)

    # Search FAISS
    D, I = index.search(query_vector, k=2) # Retrieve top 2 similar chunks

    context = ""
    for idx in I[0]:
        if idx in vector_store:
            context += " ".join(vector_store[idx][1]) + "\n\n"
    
    if not context:
        return "🤖 No relevant data found in stores documents."

    # Ask AI to generate an answer
    return llm.invoke(f"Based on the following document context, answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:")

# Streamlit Web UI
st.title("📋 AI Document Reader & Q&A Bot")
st.write("Upload a PDF and ask questions based on its content!")

# File uploader for PDF
uploaded_file = st.file_uploader("📂 Upload a PDF Document", type=["pdf"])
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    store_message = store_in_faiss(text, uploaded_file.name)
    st.write(store_message)

# User input for Q&A
query = st.text_input("❓ Ask a question based on the uploaded document:")
if query:
    answer = retrieve_and_answer(query)
    st.subheader("🤖 AI Answer:")
    st.write(answer)
