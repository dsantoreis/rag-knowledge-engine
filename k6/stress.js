import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 20,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<900']
  }
};

export default function () {
  const payload = JSON.stringify({
    question: 'How does admin monitor usage?',
    namespace: 'enterprise',
    top_k: 3
  });

  const res = http.post('http://localhost:8000/api/v1/query', payload, {
    headers: { 'Content-Type': 'application/json' }
  });

  check(res, {
    'status is 200 or 404': (r) => r.status === 200 || r.status === 404
  });

  sleep(1);
}
