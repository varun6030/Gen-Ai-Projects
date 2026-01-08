import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from rag.indexing import build_index
from rag.query_engine import query_rag

DATA_DIR = "data"

st.set_page_config(page_title="Advanced Multi-Source RAG", layout="wide")
st.title("Multi-Source RAG System")

st.header("1️⃣ Upload Documents")

uploaded_files = st.file_uploader(
    "Upload PDF or CSV files",
    type=["pdf", "csv", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    os.makedirs(DATA_DIR, exist_ok=True)

    for file in uploaded_files:
        file_path = os.path.join(DATA_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

    st.success("Files uploaded successfully.")

    if st.button("Build / Rebuild Knowledge Base"):
        with st.spinner("Building vector index..."):
            build_index()
        st.success("Knowledge base built successfully.")

st.header("2️⃣ Ask a Question")

question = st.text_input("Enter your question")

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        response = query_rag(question)

    st.subheader("Answer")
    st.write(response.response)

    st.subheader("Sources")
    for node in response.source_nodes:
        st.write(node.metadata)
