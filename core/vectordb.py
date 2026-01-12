import faiss
import numpy as np

def build_vector_db(doc_embeddings):
    """
    Runs ONCE.
    doc_embeddings: shape (num_chunks, embedding_dim)
    """

    # FAISS requires float32
    doc_embeddings = np.array(doc_embeddings).astype("float32")

    # Normalize for cosine similarity
    faiss.normalize_L2(doc_embeddings)

    # Create index
    index = faiss.IndexFlatIP(doc_embeddings.shape[1])

    # Store embeddings
    index.add(doc_embeddings)

    return index
def search_vector_db(index, query_embedding, top_k=3):
    """
    Runs EVERY QUESTION.
    query_embedding: shape (embedding_dim,)
    """

    query_embedding = np.array([query_embedding]).astype("float32")

    # Normalize query
    faiss.normalize_L2(query_embedding)

    # Search
    scores, ids = index.search(query_embedding, top_k)

    return ids[0], scores[0]


