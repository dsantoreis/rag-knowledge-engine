import { ChatPanel } from '../components/ChatPanel';
import { AdminPanel } from '../components/AdminPanel';

export default function Home() {
  return (
    <main style={{ maxWidth: 980, margin: '0 auto', padding: 24 }}>
      <h1>Portfolio Enterprise RAG Console</h1>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24 }}>
        <ChatPanel />
        <AdminPanel />
      </div>
    </main>
  );
}
