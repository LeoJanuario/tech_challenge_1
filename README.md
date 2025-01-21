# **Tech Challenge API**

Uma API RESTful desenvolvida em Python com **FastAPI**, projetada para consultar e processar dados de vitivinicultura da **Embrapa**. Este projeto é parte do **Tech Challenge** da pós-graduação.

---

## **Descrição**

A API consulta informações específicas das tabelas do site da **Embrapa**, como dados de **Produção**, **Processamento**, **Comercialização**, **Importação** e **Exportação**. O objetivo é fornecer uma base para alimentar futuros modelos de Machine Learning.

---

## **Recursos Principais**
- **Extração de dados do site da Embrapa**: Utiliza `requests` e `BeautifulSoup` para scraping de tabelas HTML específicas.
- **Fallback para CSV local**: Caso o site esteja fora do ar, os dados são obtidos de arquivos CSV locais.
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
git clone <URL_DO_REPOSITORIO>
cd tech-challenge-api
```

2. **Crie e ative o ambiente virtual:**
```bash
python -m venv venv
venv\Scripts\activate  # Para Windows
# source venv/bin/activate  # Para Linux/Mac
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**
```bash
uvicorn app.main:app --reload
```

---

## **Uso**
Acesse no navegador os seguintes endpoints:

- **API Base:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Documentação Swagger:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## **Estrutura do Projeto**


```bash
tech_challenge_api/
├── app/                 # Diretório principal da aplicação
│   ├── __init__.py      # Arquivo de inicialização do módulo
│   ├── main.py          # Arquivo principal com as rotas e lógica da API
│   ├── csvReader.py     # Módulo para leitura de arquivos CSV locais
├── csvs/                # Diretório contendo arquivos CSV locais
├── venv/                # Ambiente virtual
├── .env                 # Arquivo de variáveis de ambiente
├── .gitignore           # Arquivo para ignorar arquivos no Git
├── diagrama.puml        # Arquivo UML para visualização do projeto
├── README.md            # Documentação do projeto
├── requirements.txt     # Dependências do projeto
```


---

## **Endpoints Disponíveis**

| **Método** | **Endpoint**         | **Descrição**                                             |
|------------|----------------------|----------------------------------------------------------|
| GET        | `/producao`          | Retorna os dados de produção de vitivinicultura.         |
| GET        | `/processamento`     | Retorna os dados de processamento.                       |
| GET        | `/comercializacao`   | Retorna os dados de comercialização.                     |
| GET        | `/importacao`        | Retorna os dados de importação.                          |
| GET        | `/exportacao`        | Retorna os dados de exportação.                          |

---

## **Tecnologias Utilizadas**

- **Linguagem:** Python
- **Framework:** FastAPI
- **Bibliotecas:**
  - `requests` para requisições HTTP
  - `BeautifulSoup` para scraping de HTML
  - `Uvicorn` como servidor ASGI
  - `dotenv` para gerenciamento de variáveis de ambiente
  - `pandas` para leitura dos arquivos .csv
- **Ferramentas:**
  - VS Code
  - Swagger UI para documentação

---
