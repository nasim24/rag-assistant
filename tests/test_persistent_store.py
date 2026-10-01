from app.vectorstore.store import VectorStore


store = VectorStore()

store.load()

print(f"Documents loaded: {len(store.documents)}")
print(f"Embeddings loaded: {len(store.embeddings)}")    