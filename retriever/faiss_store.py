import numpy as np
import faiss
from retriever.doc_splitter import split_text
from retriever.embedder import get_embeddings

def get_relevant_docs(documents, query, top_k=3):
    all_chunks = []
    sources = []

    # ✅ Split documents into chunks
    for doc in documents:
        chunks = split_text(doc["content"])
        if chunks:  # Avoid empty doc crash
            all_chunks.extend(chunks)
            sources.extend([doc["filename"]] * len(chunks))

    # ✅ Get document embeddings
    doc_embeddings = get_embeddings(all_chunks)
    doc_embeddings = np.array(doc_embeddings).astype("float32")

    if doc_embeddings.size == 0:
        return "❌ No document content found for generating context."

    # ✅ Build FAISS index
    index = faiss.IndexFlatL2(doc_embeddings.shape[1])
    index.add(doc_embeddings)

    # ✅ Embed query and search
    query_embedding = get_embeddings([query])
    query_embedding = np.array(query_embedding).astype("float32")
    D, I = index.search(query_embedding, k=min(top_k, len(all_chunks)))

    # ✅ Return top-k context
    results = [all_chunks[i] for i in I[0]]
    return "\n\n".join(results)
