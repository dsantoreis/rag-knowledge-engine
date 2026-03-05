# Contributing

## Setup

```bash
# backend
cd backend && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# frontend
cd ../frontend && npm install
```

## Tests

```bash
cd backend && pytest
cd ../frontend && npm test
```

## Branching

- Branch format: `feat/*`, `fix/*`, `chore/*`
- Conventional commits required
- PR must pass CI before merge
