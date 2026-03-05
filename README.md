# RAG Knowledge Engine

Enterprise-ready RAG starter with a **Python FastAPI backend** and **Next.js frontend** (chat + admin), test suite, load test profile, Docker stack, and CI gate.

## Stack

- Backend: FastAPI + Pydantic
- Frontend: Next.js App Router (React 19)
- Tests: Pytest (unit/integration), Vitest (frontend)
- Load: k6 stress script
- Containers: multi-stage Dockerfiles + docker-compose
- CI: GitHub Actions (`.github/workflows/ci.yml`)

## Quickstart

```bash
# 1) Backend
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# 2) Frontend
cd ../frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

## API

- `GET /health`
- `POST /api/v1/ingest`
- `POST /api/v1/query`

## Tests

```bash
cd backend && pytest -q
cd ../frontend && npm test
```

## Load Test

```bash
k6 run k6/stress.js
```

## Docker

```bash
docker compose up --build
```

## Docs

- Architecture: `docs/architecture.md`
- Security: `SECURITY.md`
- Contribution guide: `CONTRIBUTING.md`
- Change history: `CHANGELOG.md`
