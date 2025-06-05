from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from retriever.faiss_store import get_relevant_docs
from langchain_pipeline.rag_chain import load_rag_chain
from dotenv import load_dotenv
import os

load_dotenv()

# ✅ Setup Hugging Face LLM with required params
llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=512,
    temperature=0.5
)

# ✅ RAG Chain setup
rag_chain = load_rag_chain(llm)

# ✅ Answer generation function
def generate_answer(question, documents):
    context = get_relevant_docs(documents, question)
    result = rag_chain.invoke({"question": question, "context": context})
    return result["text"]  # Only return the generated answer string
