from sentence_transformers import SentenceTransformer

# Load once (IMPORTANT)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    embeddings = embedding_model.encode(
        chunks,
        show_progress_bar=True
    )
    return embeddings

def embed_query(query):
    embedding = embedding_model.encode(
        query,
        show_progress_bar=False
    )
    return embedding