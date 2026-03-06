'use client';

import { useState } from 'react';
import { askQuestion, ingestDemo } from '../lib/api';

export function ChatPanel() {
  const [namespace] = useState('enterprise');
  const [question, setQuestion] = useState('How does admin monitor usage?');
  const [answer, setAnswer] = useState('');

  const run = async () => {
    await ingestDemo(namespace);
    const result = await askQuestion(namespace, question);
    setAnswer(result.answer);
  };

  return (
    <section>
      <h2>Enterprise Chat</h2>
      <input value={question} onChange={(e) => setQuestion(e.target.value)} style={{ width: '100%', padding: 10 }} />
      <button onClick={run} style={{ marginTop: 12, padding: '10px 14px', background: '#3a74ff', color: 'white', border: 0 }}>
        Ask
      </button>
      <p data-testid="answer">{answer}</p>
    </section>
  );
}
