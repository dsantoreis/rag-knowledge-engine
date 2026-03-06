from pydantic import BaseModel, Field
from typing import List


class IngestRequest(BaseModel):
    source: str = Field(..., min_length=1)
    namespace: str = Field(..., min_length=1)
    chunk_size: int = 512
    chunk_overlap: int = 50


class SourceRef(BaseModel):
    document: str
    page: int
    score: float


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3)
    namespace: str
    top_k: int = 5


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceRef]
    latency_ms: int
