import time
from fastapi import FastAPI, HTTPException
from .models import IngestRequest, QueryRequest, QueryResponse, SourceRef
from .store import store

app = FastAPI(title="RAG Knowledge Engine", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/v1/ingest")
def ingest(payload: IngestRequest):
    inserted = store.ingest(
        namespace=payload.namespace,
        source=payload.source,
        text=(
            "Enterprise portfolio includes secure chat, compliance dashboards, and tenant analytics. "
            "Admin users can monitor usage and search quality. "
            "The platform supports Docker deployments with CI validation."
        ),
    )
    return {"ingested_chunks": inserted, "namespace": payload.namespace}


@app.post("/api/v1/query", response_model=QueryResponse)
def query(payload: QueryRequest):
    start = time.time()
    matches = store.search(payload.namespace, payload.question, payload.top_k)
    if not matches:
        raise HTTPException(status_code=404, detail="No relevant context found")

    sources = [
        SourceRef(document=item.source, page=item.page, score=round(score, 3))
        for score, item in matches
    ]
    answer = " ".join(item.text for _, item in matches)
    return QueryResponse(answer=answer, sources=sources, latency_ms=int((time.time() - start) * 1000))
