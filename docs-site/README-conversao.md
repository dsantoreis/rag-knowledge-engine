# Cortex Docs — Conversão para Astro Starlight

![Hero](./public/assets/hero.svg)

![Demo GIF](./public/assets/demo.gif)

[![Docs CI](https://img.shields.io/github/actions/workflow/status/dsantoreis/cortex/docs-site.yml?branch=main)](../../actions/workflows/docs-site.yml)

## Quickstart

```bash
npm ci
npm run dev
npm run build
```

## Architecture

```mermaid
flowchart LR
 UI[Next.js UI] --> API[Python RAG API]
 API --> VDB[(Vector DB)]
 API --> LLM[LLM Provider]
```

## Benchmarks

- Static docs build under 3s local
- CDN-ready output for low-latency delivery

## Docker

```bash
docker build -t cortex-docs:latest .
docker compose up --build
```

## Kubernetes

```bash
kubectl apply -f k8s/
```

⭐ Star the repo if this docs setup accelerates your rollout.
