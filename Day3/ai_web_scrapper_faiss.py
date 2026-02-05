import requests
from bs4 import BeautifulSoup
import streamlit as st
import faiss
import numpy as np
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
# Importaciones previas de LangChain versión 0.2.x ⬇️⬇️⬇️
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.schema import Document
# Importaciones actualizadas ⬇️⬇️⬇️
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

# Load AI Model
llm = OllamaLLM(model="mistral") # Change to "llama3" or another Ollama model

# Load Hugging Face Embeddings 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize FAISS Vector Database
index = faiss.IndexFlatL2(384) # Vector dimension for MiniLM
vector_store = {}