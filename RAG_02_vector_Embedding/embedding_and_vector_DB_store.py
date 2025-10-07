import requests
import numpy as np
import faiss
import os
from dotenv import load_dotenv
from utils.utils import generate_embeddings

# Load environment variables from .env file
load_dotenv()


api_key=os.getenv('euri_api_key')
# api_key

def create_vector_DB(text_content):
    dimension = 1536
    index = faiss.IndexFlatL2(dimension)

    chunk_mapping = []
    for chunk in text_content:
        emb = generate_embeddings(chunk)
        # print(emb)
        index.add(np.array([emb]).astype("float32"))
        chunk_mapping.append(chunk)
    
    faiss.write_index(index,"vector_database/index.faiss")

    return index,chunk_mapping

def chunks_map(text_content):
    chunk_mapping = []
    for chunk in text_content:
        chunk_mapping.append(chunk)
    return chunk_mapping