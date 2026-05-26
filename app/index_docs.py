import json

from app.services.embeddings import get_embedding
from app.vectorstore.faiss_store import add_to_index

with open("docs.json", "r") as f:

    docs = json.load(f)

documents = []

embeddings = []

for doc in docs:

    embedding = get_embedding(doc["text"])

    embeddings.append(embedding)

    documents.append(doc["text"])

add_to_index(
    embeddings,
    documents
)

print("Documents Indexed Successfully")