from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_statusz_includes_version_and_uptime():
    res = client.get("/statusz")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "ok"
    assert body["version"] == "0.1.0"
    assert isinstance(body["uptime_sec"], int)
    assert body["uptime_sec"] >= 0


def test_readyz_reports_store_stats():
    baseline = client.get("/readyz")
    assert baseline.status_code == 200
    base_body = baseline.json()

    ing = client.post(
        "/api/v1/ingest",
        json={"source": "readyz.md", "namespace": "readyz-test", "chunk_size": 512, "chunk_overlap": 50},
    )
    assert ing.status_code == 200

    after = client.get("/readyz")
    assert after.status_code == 200
    body = after.json()
    assert body["ready"] is True
    assert body["namespaces"] >= base_body["namespaces"]
    assert body["chunks"] > base_body["chunks"]


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
