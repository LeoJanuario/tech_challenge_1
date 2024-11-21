# **Tech Challenge API**

Uma API RESTful desenvolvida em Python com **FastAPI**, projetada para consultar e processar dados de vitivinicultura da **Embrapa**. Este projeto é parte do **Tech Challenge** da pós-graduação.

---

## **Descrição**

A API consulta informações específicas das tabelas do site da **Embrapa**, como dados de **Produção**, **Processamento**, **Comercialização**, **Importação** e **Exportação**. O objetivo é fornecer uma base para alimentar futuros modelos de Machine Learning.

---

## **Recursos Principais**
- **Extração de dados do site da Embrapa**: Utiliza `requests` e `BeautifulSoup` para scraping de tabelas HTML específicas.
- **Endpoints RESTful**: Endpoints organizados para cada tipo de dado.
- **Documentação Automática**: Swagger UI disponível em `/docs`.
- **Desenvolvimento Ágil**: Suporte para recarga automática no modo desenvolvimento (`--reload`).


---

## **Pré-requisitos**
Antes de iniciar o projeto, instale as seguintes ferramentas:
- Python 3.10 ou superior
- Git

---

## **Configuração do Projeto**

1. **Clone o repositório:**
    ```bash
    git clone (url Projeto)
    cd tech-challenge-api
    python -m venv venv
    ```

2. **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute a aplicação:**
    ```bash
    uvicorn app.main:app --reload
    ```

## Acesse no navegador:

- **API Base:** http://127.0.0.1:8000
- **Documentação Swagger:** http://127.0.0.1:8000/docs

## Estrutura do Projeto

```bash
tech_challenge_api/
├── app/
│   ├── __init__.py         # Arquivo de inicialização do módulo
│   ├── main.py             # Arquivo principal com as rotas e lógica da API
├── venv/                   # Ambiente virtual
├── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto
```


# Endpoints Disponíveis

| **Método** | **Endpoint**         | **Descrição**                                             |
|------------|----------------------|----------------------------------------------------------|
| GET        | `/producao`          | Retorna os dados de produção de vitivinicultura.         |
| GET        | `/processamento`     | Retorna os dados de processamento.                       |
| GET        | `/comercializacao`   | Retorna os dados de comercialização.                     |
| GET        | `/Importacao`        | Retorna os dados de importação.                          |
| GET        | `/Exportacao`        | Retorna os dados de exportação.                          |


## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** FastAPI
- **Bibliotecas:**
  - `requests` para requisições HTTP
  - `BeautifulSoup` para scraping de HTML
  - `Uvicorn` como servidor ASGI
- **Ferramentas:**
  - VS Code
  - Swagger UI para documentação
