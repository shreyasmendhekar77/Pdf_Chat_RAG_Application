from euriai.langchain import create_chat_model
import requests
import numpy as np
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()


api_key=os.getenv('euri_api_key')

def chat_model_fun():
    chat_model = create_chat_model(
        api_key=api_key,
        model="gpt-4.1-nano",
        temperature=0.7
    )
    return chat_model



def generate_completion(prompt):
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 1500,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    data=data['choices'][0]['message']['content']
    return data



def generate_embeddings(text):
    url = "https://api.euron.one/api/v1/euri/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }
    payload = {
        "input": text,
        "model": "text-embedding-3-small"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    embedding = np.array(data['data'][0]['embedding'])
    
    return embedding