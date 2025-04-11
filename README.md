# 🧪 Testes de Performance

Este repositório contém os scripts, cenários e configurações utilizados para realizar **testes de performance** em nossos serviços/sistemas. O objetivo é garantir que as aplicações mantenham um desempenho aceitável sob diferentes cargas de uso.

---

## Tipos de Testes

- Stress: Executar teste com uma carga muito alta
- Carga: Executar o teste com uma carga moderada
- Picos: Executar teste provocandouma carga muito alta em um curto período de tempo
- Resiliência: Executar testes com carga moderada por um longo período
- Escalabilidade: Executar teste controlando o aumento de carga

---

## 📌 Objetivos

- Avaliar o comportamento do sistema sob diferentes níveis de carga
- Identificar gargalos de performance
- Medir tempo de resposta, throughput, uso de CPU/memória, entre outros
- Validar escalabilidade e resiliência

---

## 🛠️ Ferramentas Utilizadas

- Ferramentas de teste de performance: JMeter, k6, Gatling, Artillery.
- Ferramentas de monitoramento: Grafana, Prometheus, New Relic, Datadog.
- Outros: Docker, Kubernetes

---

## 📁 Estrutura do Repositório

```
.
├── scenarios/               # Cenários de teste (ex: carga leve, carga pesada)
├── scripts/                 # Scripts de teste (HTTP, gRPC, WebSocket, etc.)
│   ├── smoke.js             # Teste rápido (sanidade)
│   ├── stress.js            # Estresse pesado
|   ├── carga.js             # Carga moderada
|   ├── picos.js             # Avaliar a resposta do sistema a picos súbitos
|   ├── resiliência.js       # Testar a capacidade do sistema de manter um desempenho estável
│   └── escalabilidade.js    # Avaliar a capacidade do sistema em crescer e lidar com aumento de carga
├── data/                    # Dados externos (CSV, JSON, etc.)
├── results/                 # Resultados dos testes
├── reports/                 # Relatórios gerados (HTML, JSON, CSV, etc.)
├── config/                  # Configurações (ex: variáveis de ambiente)
└── README.md                # Este arquivo
```

---

## 🚀 Como Instalar e Executar os Testes

```bash
# 1. Instale o K6
sudo gpg -k
sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update
sudo apt-get install k6

# 2. Execute o teste
[k6 run scripts/carga.js]

# 3. Verifique os relatórios
[Verificar o output]
```

---

## 📊 Interpretação dos Resultados

- **Throughput (RPS)**: Quantidade de requisições por segundo.
- **Latency**: Tempo de resposta das requisições (médio, p95, p99).
- **Erros**: Percentual de erros e tipos (ex: timeouts, 5xx, etc).
- **Recursos**: Uso de CPU, memória, rede (se monitorado).

---

## 🧠 Boas Práticas

- Comece com testes pequenos e vá aumentando gradualmente a carga
- Execute testes em ambientes isolados e controlados
- Documente todos os parâmetros do teste
- Automatize execuções e geração de relatórios quando possível

---

## 📌 Contato

Para dúvidas ou sugestões, entre em contato com:

- Nome do responsável: [Nome ou equipe]
- Email: [horadoqa@gmail.com]
- Discord: [ttps://discord.gg/8h2HHdKPe5]

---
