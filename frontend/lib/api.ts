const API_BASE = process.env.NEXT_PUBLIC_API_BASE ?? 'http://localhost:8000';

export async function ingestDemo(namespace: string) {
  const res = await fetch(`${API_BASE}/api/v1/ingest`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ source: 'portfolio.md', namespace, chunk_size: 512, chunk_overlap: 50 })
  });
  if (!res.ok) throw new Error('ingest failed');
  return res.json();
}

export async function askQuestion(namespace: string, question: string) {
  const res = await fetch(`${API_BASE}/api/v1/query`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ namespace, question, top_k: 5 })
  });
  if (!res.ok) throw new Error('query failed');
  return res.json();
}
