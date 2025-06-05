# File upload and parsing logic
import os
import streamlit as st
from PyPDF2 import PdfReader

def handle_file_upload():
    uploaded_files = st.file_uploader("Upload PDF/DOCX/CSV files", type=["pdf"], accept_multiple_files=True)
    docs = []
    for file in uploaded_files:
        reader = PdfReader(file)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        docs.append({"filename": file.name, "content": text})
    return docs