import json
import numpy as np


class VectorStore:

    def __init__(self):
        self.documents = []
        self.embeddings = []

    def add(self, text: str, embedding: list[float], metadata: dict = None):
        self.documents.append({
            "text": text,
            "metadata": metadata or {}
        })

        self.embeddings.append(embedding)

    def search(self, query_embedding: list[float], top_k: int = 3):
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
            np.linalg.norm(vector_a) *
            np.linalg.norm(vector_b)
        )