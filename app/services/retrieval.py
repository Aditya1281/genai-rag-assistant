from app.services.embeddings import get_embedding
from app.vectorstore.faiss_store import search_index

def retrieve_chunks(query):

    query_embedding = get_embedding(query)

    results = search_index(query_embedding)

    return results