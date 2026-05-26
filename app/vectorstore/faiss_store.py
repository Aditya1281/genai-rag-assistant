import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

stored_docs = []

def add_to_index(vectors, documents):

    global stored_docs

    vector = np.array(
        vectors,
        dtype="float32"
    )

    vector = vector.reshape(
        len(vectors),
        dimension
    )

    index.add(vector)

    stored_docs.extend(documents)

def search_index(query_vector, top_k=3):

    query_vector = np.array(
        [query_vector],
        dtype="float32"
    )

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(stored_docs):

            results.append(
                stored_docs[idx]
            )

    return results