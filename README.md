# 🏎️ F1 Dashboard

Dashboard de visualização de dados da Fórmula 1 com 75 anos de história (1950–2026), construído como projeto pessoal de estudo em engenharia de dados e visualização.

> **Nota:** Este é um projeto pessoal escrito sem uso direto de inteligência artificial. Todo o código foi desenvolvido manualmente, com o objetivo de consolidar conhecimentos práticos em engenharia de dados, construção de pipelines ELT, desenvolvimento de APIs e visualização de dados.

---

## 📌 Sobre o Projeto

O F1 Dashboard nasceu como um projeto de portfólio para colocar em prática conceitos de engenharia de dados em um ambiente próximo ao de produção. A ideia é cobrir o ciclo completo de dados: desde a ingestão dos CSVs brutos até a visualização interativa no navegador, passando por um pipeline ELT, um banco de dados relacional e uma API REST.

Os dados utilizados são do dataset público [Formula 1 Complete Dataset (1950–2026)](https://www.kaggle.com/datasets/patelris/formula-1-complete-dataset-1950-2026) disponível no Kaggle, cobrindo corridas, pilotos, equipes, resultados, qualificações e standings ao longo de 75 temporadas.

**O que o projeto cobre:**

- Pipeline ELT com ingestão, carga e transformação de dados reais
- Armazenamento em banco de dados relacional com separação entre dados brutos e processados
- Exportação de dados processados em formato Parquet
- API REST para servir os dados ao frontend
- Dashboard web interativo com visualizações e filtros

---

## 🗂️ Arquitetura do Projeto

```
F1_Dashboard/
├── api/                   # API FastAPI
│   └── main.py
├── data/
│   ├── raw/               # CSVs originais do Kaggle
│   └── processed/         # Dados limpos em formato Parquet
├── docker/
│   └── Dockerfile
├── elt/                   # Pipeline ELT
│   ├── config.py          # Configuração de paths e banco de dados
│   ├── extract.py         # Leitura dos CSVs para DataFrames
│   ├── load.py            # Carga no schema raw do PostgreSQL
│   ├── transform.py       # Limpeza e persistência no schema processed
│   └── run_pipeline.py    # Entry point do pipeline
├── frontend/
│   └── src/               # Dashboard web
├── .env                   # Variáveis de ambiente
├── .gitignore
└── docker-compose.yml     # PostgreSQL + API
```

**Fluxo de dados:**

```
data/raw/*.csv
      │
      ▼
[Extract] — lê os CSVs com pandas
      │
      ▼
[Load] — persiste no schema raw do PostgreSQL (dados brutos, sem alteração)
      │
      ▼
[Transform] — limpa, tipifica e persiste no schema processed (PostgreSQL + Parquet)
      │
      ▼
[API FastAPI] — serve os dados do schema processed via endpoints REST
      │
      ▼
[Frontend] — consome a API e exibe visualizações interativas
```

O banco de dados PostgreSQL é dividido em dois schemas:

- `raw` — dados exatamente como vieram dos CSVs, sem qualquer modificação
- `processed` — dados limpos, com tipos corrigidos, nulos tratados e colunas desnecessárias removidas

---

## ▶️ Como Rodar

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.12+
- WSL (Windows) ou Linux/macOS
- Dataset do Kaggle baixado em `data/raw/`

### 1. Clone o repositório

```bash
git clone https://github.com/henriquerodrigues13/F1_Dashboard.git
cd F1_Dashboard
```

### 2. Configure as variáveis de ambiente

Crie o arquivo `.env` na raiz do projeto:

```env
POSTGRES_USER=f1_user
POSTGRES_PASSWORD=f1_password
POSTGRES_DB=f1_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DATABASE_URL=postgresql://f1_user:f1_password@localhost:5432/f1_db
```

### 3. Instale as dependências Python

```bash
pip3 install -r requirements.txt
```

### 4. Suba o banco de dados

```bash
docker compose up -d postgres
```

### 5. Rode o pipeline ELT

```bash
python3 elt/run_pipeline.py
```

O pipeline vai:
1. Ler os 8 CSVs de `data/raw/`
2. Carregar os dados brutos no schema `raw` do PostgreSQL
3. Limpar e transformar os dados no schema `processed`
4. Salvar os dados processados em `data/processed/*.parquet`

### 6. Valide os dados com DuckDB

```bash
pip3 install duckdb
duckdb
```

```sql
SELECT * FROM 'data/processed/drivers.parquet' LIMIT 10;
```

### 7. Suba a API

```bash
docker compose up -d
```

A API estará disponível em `http://localhost:8000` e a documentação interativa em `http://localhost:8000/docs`.

---

## 🛠️ Decisões de Tecnologia

### Python + Pandas
Linguagem central do projeto. O pandas foi escolhido para manipulação dos DataFrames na etapa de extração e transformação por ser a biblioteca padrão do ecossistema de dados em Python, com integração nativa com PostgreSQL via SQLAlchemy e suporte direto a Parquet via PyArrow.

### PostgreSQL
Banco de dados relacional escolhido por ser o padrão de mercado em ambientes de produção de dados. A separação em dois schemas (`raw` e `processed`) é uma prática de engenharia de dados que preserva os dados originais intactos e permite reprocessar as transformações sem precisar re-ingerir os dados.

### Parquet + PyArrow
Os dados processados são exportados em formato Parquet além de persistidos no PostgreSQL. Parquet é o formato colunar padrão do mercado para dados analíticos — comprimido, rápido de ler e compatível com todo o ecossistema de big data (Spark, DuckDB, BigQuery, Redshift). O PyArrow é o backend utilizado pelo pandas para leitura e escrita de Parquet.

### DuckDB
Utilizado para inspeção dos arquivos Parquet diretamente no terminal durante o desenvolvimento. Permite rodar SQL sobre os arquivos `.parquet` sem precisar de nenhum servidor, o que torna o ciclo de validação dos dados mais rápido.

### FastAPI
Framework web escolhido para a API REST por ser assíncrono, moderno e ter integração nativa com Pydantic para validação de dados e geração automática de documentação via Swagger. Já fazia parte da stack do projeto e é amplamente adotado em ambientes de produção.

### Docker + Docker Compose
Todo o ambiente é containerizado para garantir reprodutibilidade e uma experiência próxima à de produção desde o desenvolvimento local. O PostgreSQL roda em container com volume persistente, e a API também é servida via Docker Compose.

### SQLAlchemy
Usado como camada de abstração para conexão com o PostgreSQL tanto no pipeline ELT quanto na API. Permite flexibilidade para mudar de banco de dados sem alterar a lógica da aplicação.
