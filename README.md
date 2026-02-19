# ⚡ EnergyHub

**EnergyHub** é uma plataforma modular de monitoramento, simulação e previsão de consumo energético residencial.

O projeto combina dados reais de faturas com modelos estimativos baseados em equipamentos para fornecer inteligência energética prática, auditável e escalável.

---

## 🎯 Objetivo

Permitir que usuários acompanhem, analisem e projetem seu consumo de energia elétrica de forma estruturada, transformando dados brutos de contas mensais em informações estratégicas para tomada de decisão.

---

## 🏗 Arquitetura

EnergyHub é dividido em dois blocos principais:

### 🔹 Backend (Raspberry Pi)
- API REST com FastAPI
- Banco de dados relacional
- Camada de simulação e previsão
- Persistência de histórico
- Processamento e calibração

### 🔹 Interface Local (ESP32)
- Dashboard de visualização
- Consulta de consumo e projeções
- Operação sob demanda e baixo consumo

Arquitetura projetada para crescimento modular e integração futura com sensores, dispositivos IoT e aplicações móveis.

---

## 📦 Funcionalidades (Fase 1)

- Cadastro de contas de energia
- Cadastro de equipamentos elétricos
- Armazenamento estruturado de consumo mensal
- Base preparada para simulação e previsão

---

Organização modular para manter separação clara entre:
- Camada de dados
- Lógica de negócio
- Interface de API
- Serviços futuros (simulação, previsão)

---

## 🧰 Gerenciamento de Dependências

O projeto utiliza **uv** para gerenciamento de ambiente e dependências.

### Instalação do uv

Consulte a documentação oficial para instalação:

https://github.com/astral-sh/uv

---

## 🚀 Configuração do Ambiente

Criar ambiente virtual e instalar dependências:

- uv venv
- uv sync

Adicionar novas dependências:
- uv add fastapi
- uv add sqlalchemy
- uv add alembic
- uv add uvicorn


As dependências são gerenciadas via `pyproject.toml`.

---

---

## 🗄 Modelo de Dados Inicial

### `bills`
Armazena o consumo real mensal.

Campos principais:
- reference_month
- consumption_kwh
- total_value
- tariff_value

### `appliances`
Cadastro de equipamentos para simulação futura.

Campos principais:
- name
- nominal_power_w
- average_hours_per_day
- active

---

## 🛣 Roadmap

### Fase 1
CRUD completo e persistência estável.

### Fase 2
Motor de simulação baseado em potência × tempo de uso.

### Fase 3
Calibração automática com base no consumo real.

### Fase 4
Previsão mensal com análise de tendência e sazonalidade.

### Fase 5
Dashboard embarcado e alertas inteligentes.

---

## 🔐 Licença

Distribuído sob a licença **Apache License 2.0**.

Consulte o arquivo `LICENSE` para mais informações.

---

## 📌 Status do Projeto

Em desenvolvimento ativo.
Arquitetura pensada para uso real em ambiente residencial com possibilidade de expansão futura.

---

**EnergyHub**  
Monitoramento energético com inteligência, estrutura e previsibilidade.


