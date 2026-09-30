import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text"

def create_embedding(text: str) -> list[float]:
    response = requests.post(
        OLLAMA_URL, 
        json={
            "model": MODEL,
            "prompt": text
        }, 
    )

    response.raise_for_status()
    data = response.json()
    
    return data["embedding"]