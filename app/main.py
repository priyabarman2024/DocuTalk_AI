# Entry point: Streamlit
import sys
import os
import asyncio
os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNINGS"] = "true"
# Ensure parent directory is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Async loop fix for Streamlit + LangChain
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

import streamlit as st
from chatbot import generate_answer
from file_uploader import handle_file_upload
from user_auth import login_user

# Streamlit UI Config
st.set_page_config(page_title="DocuTalk AI", layout="wide")

# Login
if not login_user():
    st.stop()

# Upload documents
uploaded_docs = handle_file_upload()

# User interaction
st.title("📄 DocuTalk AI: Chat with your documents")
question = st.text_input("Ask a question about the uploaded documents")

if question and uploaded_docs:
    with st.spinner("Generating answer..."):
        try:
            response = generate_answer(question, uploaded_docs)
            st.markdown("### 💬 Answer:")
            st.markdown(response)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")