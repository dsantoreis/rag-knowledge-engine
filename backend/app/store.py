from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Chunk:
    source: str
    text: str
    page: int


class InMemoryStore:
    def __init__(self) -> None:
        self._db: Dict[str, List[Chunk]] = defaultdict(list)

    def ingest(self, namespace: str, source: str, text: str) -> int:
        chunks = [part.strip() for part in text.split(".") if part.strip()]
        for idx, chunk in enumerate(chunks, start=1):
            self._db[namespace].append(Chunk(source=source, text=chunk, page=idx))
        return len(chunks)

    def search(self, namespace: str, question: str, top_k: int):
        corpus = self._db.get(namespace, [])
        q_terms = set(question.lower().split())
        scored = []
        for chunk in corpus:
            c_terms = set(chunk.text.lower().split())
            overlap = len(q_terms & c_terms)
            if overlap > 0:
                scored.append((overlap / max(len(q_terms), 1), chunk))
        scored.sort(key=lambda item: item[0], reverse=True)
        return scored[:top_k]


store = InMemoryStore()
