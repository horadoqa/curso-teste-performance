import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 10 }, // subida para 10 usuários em 30s
    { duration: '1m', target: 10 },  // mantém por 1 minuto
    { duration: '30s', target: 0 },  // rampa de saída
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% das requisições devem durar < 500ms
    http_req_failed: ['rate<0.03'],   // menos de 3% de falhas
  },
};

export default function () {
  const res = http.get('https://test-api.k6.io/public/crocodiles/');

  check(res, {
    'status é 200': (r) => r.status === 200,
    'tempo de resposta < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1); // pausa de 1s entre as requisições
}
