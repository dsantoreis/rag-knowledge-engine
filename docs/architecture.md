# Portfolio Enterprise Architecture

- **Backend**: FastAPI API for ingest/query and lightweight retrieval
- **Frontend**: Next.js app router with chat and admin views
- **Testing**: Pytest + Vitest + k6 load profile
- **Containers**: Multi-stage Docker for backend/frontend and compose for local stack
- **CI**: GitHub Actions workflow with Python + Node gates
