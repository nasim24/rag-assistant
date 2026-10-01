from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.embeddings.embedder import create_embedding
from app.vectorstore.store import VectorStore


PDF_PATH = "documents/sample.pdf"


# -----------------------------------
# INGESTION
# -----------------------------------

text = load_pdf(PDF_PATH)

print(f"Loaded characters: {len(text)}")

chunks = chunk_text(text)

print(f"Created chunks: {len(chunks)}")


# -----------------------------------
# CREATE VECTOR STORE
# -----------------------------------

store = VectorStore()


for index, chunk in enumerate(chunks):

    print(
        f"Creating embedding "
        f"{index + 1}/{len(chunks)}"
    )

    embedding = create_embedding(chunk)

    store.add(
        text=chunk,
        embedding=embedding,
        metadata={
            "source": "sample.pdf",
            "chunk_index": index
        }
    )


# -----------------------------------
# SAVE
# -----------------------------------

store.save()