from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.embeddings.embedder import create_embedding
from app.vectorstore.store import VectorStore


PDF_PATH = "documents/sample.pdf"


# 1. Load PDF
text = load_pdf(PDF_PATH)

print(f"Loaded characters: {len(text)}")


# 2. Chunk PDF
chunks = chunk_text(text)

print(f"Created chunks: {len(chunks)}")


# 3. Create vector store
store = VectorStore()


# 4. Embed every chunk
for index, chunk in enumerate(chunks):

    print(f"Creating embedding {index + 1}/{len(chunks)}")

    embedding = create_embedding(chunk)

    store.add(
        text=chunk,
        embedding=embedding,
        metadata={
            "source": "sample.pdf",
            "chunk_index": index
        }
    )


print("\nVector store ready!")


# 5. Test semantic search
query = "What is AI engineer?"

query_embedding = create_embedding(query)

results = store.search(
    query_embedding=query_embedding,
    top_k=3
)


print("\nSearch Results:")

for result in results:

    print("\n-------------------------")
    print(f"Score: {result['score']:.4f}")
    print(f"Metadata: {result['metadata']}")
    print(result["text"][:500])