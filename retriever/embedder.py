from sentence_transformers import SentenceTransformer
import numpy as np

# ✅ Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(chunks):
    """
    Encode a list of text chunks into dense embeddings.
    
    Args:
        chunks (List[str]): List of text strings.

    Returns:
        List[List[float]]: List of embedding vectors.
    """
    if not chunks:
        return []
    embeddings = model.encode(chunks, show_progress_bar=False, convert_to_numpy=True, normalize_embeddings=True)
    return embeddings.tolist()
