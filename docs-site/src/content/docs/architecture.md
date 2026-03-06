---
title: Architecture
---

```mermaid
flowchart LR
 UI[Next.js UI] --> API[Python RAG API]
 API --> VDB[(Vector DB)]
 API --> LLM[LLM Provider]
```
