from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_ingest_and_query_integration():
    ing = client.post(
        "/api/v1/ingest",
        json={"source": "portfolio.md", "namespace": "enterprise", "chunk_size": 512, "chunk_overlap": 50},
    )
    assert ing.status_code == 200
    assert ing.json()["ingested_chunks"] > 0

    q = client.post(
        "/api/v1/query",
        json={"question": "How does admin monitor usage?", "namespace": "enterprise", "top_k": 3},
    )
    assert q.status_code == 200
    body = q.json()
    assert "Admin users" in body["answer"]
    assert len(body["sources"]) >= 1
