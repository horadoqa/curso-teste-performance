import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 1 },  // mantém por 1 minuto
  ],
  thresholds: {
    http_req_duration: ['p(95)<2000'], // 95% das requisições devem durar < 500ms
    http_req_failed: ['rate<0.03'],   // menos de 3% de falhas
  },
};

export default function () {
  const res = http.get('https://test-api.k6.io/public/crocodiles/');

  check(res, {
    'status é 200': (r) => r.status === 200,
    'tempo de resposta < 400ms': (r) => r.timings.duration < 400,
  });

  sleep(1); // pausa de 1s entre as requisições
}
