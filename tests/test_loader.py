from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text


pdf_path = "documents/sample.pdf"

text = load_pdf(pdf_path)

chunks = chunk_text(text)

print(f"Total characters: {len(text)}")
print(f"Total chunks: {len(chunks)}")

for index, chunk in enumerate(chunks, start=1):
    print(f"\n===== CHUNK {index} =====")
    print(chunk)