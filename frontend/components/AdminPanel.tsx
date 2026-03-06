import React from 'react';

export function AdminPanel() {
  return (
    <section>
      <h2>Admin</h2>
      <ul>
        <li>Namespaces: 1</li>
        <li>RAG latency target: &lt; 800ms p95</li>
        <li>CI gate: unit + integration + build</li>
      </ul>
    </section>
  );
}
