from app.embeddings.embedder import create_embedding


text = "Laravel is a PHP framework for building web applications."

embedding = create_embedding(text)

print(f"Embedding dimensions: {len(embedding)}")
print(f"First 10 values: {embedding[:10]}")