# RAG Knowledge Engine

[![CI](../../actions/workflows/ci.yml/badge.svg)](#) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)


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

## Kubernetes

```bash
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
kubectl apply -f k8s/ingress.yaml
```

## Docs

- Architecture: `docs/architecture.md`
- Security: `SECURITY.md`
- Contribution guide: `CONTRIBUTING.md`
- Change history: `CHANGELOG.md`


## Conversion Standard

### Hero
Production-ready solution for a concrete business problem with measurable outcome.

### Problem
Describe the pain with one sentence and a real operator context.

### Demo
Add a GIF at `docs/assets/demo.gif` and reference it here.

### Quickstart (3 commands)
```bash
make setup || pnpm install || npm install
make test || pnpm test || npm test
make run || pnpm dev || npm run dev
```

### Architecture
Document API, workers, and storage in `docs/architecture.md`.

### Results
Add benchmark, latency, throughput, or conversion impact.

### Roadmap
Include 30-day and 90-day milestones.

### CTA
If this helps, star the repo and open an issue with your use case.
