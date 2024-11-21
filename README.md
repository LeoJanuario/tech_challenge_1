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

3. **Execute a aplicação:**
    ```bash
    uvicorn app.main:app --reload
    ```