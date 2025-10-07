import numpy as np
from utils.utils import generate_embeddings


def build_prompt(context_chunks, query):
    context = "\n\n".join(context_chunks)
    return f"""Use the context below to answer the question.

            Context:
            {context}

            Question:
            {query}

            Answer:"""


def retrieve_top_k(query,vector_db,chunks):
    query_embedding = generate_embeddings(query)
    distances, indices = vector_db.search(np.array([query_embedding]).astype("float32"), 3)
    return [chunks[i] for i in indices[0]]