import json
import os

import numpy as np


class VectorStore:

    def __init__(self, storage_path: str = "data/vector_store.json"):
        self.storage_path = storage_path
        self.documents = []
        self.embeddings = []

    def add(
        self,
        text: str,
        embedding: list[float],
        metadata: dict = None
    ):
        self.documents.append({
            "text": text,
            "metadata": metadata or {}
        })

        self.embeddings.append(embedding)

    def save(self):
        data = {
            "documents": self.documents,
            "embeddings": self.embeddings
        }

        directory = os.path.dirname(self.storage_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

        print(f"Vector store saved to: {self.storage_path}")

    def load(self):
        if not os.path.exists(self.storage_path):
            print("No existing vector store found.")
            return

        with open(self.storage_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.documents = data["documents"]
        self.embeddings = data["embeddings"]

        print(
            f"Loaded {len(self.documents)} documents "
            f"from vector store."
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 3
    ):
        if not self.embeddings:
            return []

        query_vector = np.array(query_embedding)

        scores = []

        for index, embedding in enumerate(self.embeddings):

            document_vector = np.array(embedding)

            score = self._cosine_similarity(
                query_vector,
                document_vector
            )

            scores.append({
                "text": self.documents[index]["text"],
                "metadata": self.documents[index]["metadata"],
                "score": float(score)
            })

        scores.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return scores[:top_k]

    @staticmethod
    def _cosine_similarity(vector_a, vector_b):

        return np.dot(vector_a, vector_b) / (
            np.linalg.norm(vector_a)
            * np.linalg.norm(vector_b)
        )