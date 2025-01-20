from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

### Rota para retornar dados da aba de produção no site VitiBrasil
@app.get("/producao")
def get_producao(ano: int = Query(2023, description="Ano para filtrar os dados")):

    base_url = os.getenv("url_base") 
    opcao = "opt_02"

    url = f"{base_url}?&ano={ano}&opcao={opcao}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Não foi possível acessar o site"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Tabela não encontrada"}
    
    headers = [header.text.strip() for header in table.find_all("th")]

    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = [col.text.strip() for col in row.find_all("td")]
        if cols:
            data.append(cols)

    return {
        "ano": ano,
        "headers": headers,
        "data": data
    }

@app.get("/comercializacao")
def get_comercializacao(ano: int = Query(2023, description="Ano para filtrar os dados")):
    
    base_url = os.getenv("url_base") 
    opcao = "opt_04"
    url = f"{base_url}?&ano={ano}&opcao={opcao}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Não foi possível acessar o site"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Tabela não encontrada"}
    
    headers = [header.text.strip() for header in table.find_all("th")]

    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = [col.text.strip() for col in row.find_all("td")]
        if cols:
            data.append(cols)

    return {
        "ano": ano,
        "headers": headers,
        "data": data
    }

@app.get("/processamento")
def get_processamento(ano: int = Query(2023, description="Ano para filtrar os dados")):
   
    base_url = os.getenv("url_base")
    subopcoes = [f"subopt_0{i}" for i in range(1, 5)]  # subopt_01 a subopt_04
    opcao = "opt_03"

    all_data = []

    for subopcao in subopcoes:
        # Construir a URL dinâmica
        url = f"{base_url}?ano={ano}&opcao={opcao}&subopcao={subopcao}"
        response = requests.get(url)

        if response.status_code != 200:
            all_data.append({"subopcao": subopcao, "error": "Não foi possível acessar o site"})
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", {"class": "tb_base tb_dados"})

        if not tables:
            all_data.append({"subopcao": subopcao, "error": "Nenhuma tabela encontrada"})
            continue

        subopcao_data = {"subopcao": subopcao, "tables": []}
        for table in tables:
            title = table.find_previous("h3") or table.find_previous("h2") or table.find_previous("p")
            title_text = title.text.strip() if title else f"Tabela {len(subopcao_data['tables']) + 1}"

            headers = [header.text.strip() for header in table.find_all("th")]

            rows = table.find_all("tr")
            data = []
            for row in rows:
                cols = [col.text.strip() for col in row.find_all("td")]
                if cols:
                    data.append(cols)

            subopcao_data["tables"].append({
                "title": title_text,
                "headers": headers,
                "data": data
            })

        all_data.append(subopcao_data)

    return {"ano": ano, "data": all_data}

@app.get("/importacao")
def get_importacao(ano: int = Query(2023, description="Ano para filtrar os dados")):
    
    base_url = os.getenv("url_base")
    subopcoes = [f"subopt_0{i}" for i in range(1, 5)]  # subopt_01 a subopt_04
    opcao = "opt_05"

    all_data = []

    for subopcao in subopcoes:
        # Construir a URL dinâmica
        url = f"{base_url}?ano={ano}&opcao={opcao}&subopcao={subopcao}"
        response = requests.get(url)

        if response.status_code != 200:
            all_data.append({"subopcao": subopcao, "error": "Não foi possível acessar o site"})
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", {"class": "tb_base tb_dados"})

        if not tables:
            all_data.append({"subopcao": subopcao, "error": "Nenhuma tabela encontrada"})
            continue

        subopcao_data = {"subopcao": subopcao, "tables": []}
        for table in tables:
            title = table.find_previous("h3") or table.find_previous("h2") or table.find_previous("p")
            title_text = title.text.strip() if title else f"Tabela {len(subopcao_data['tables']) + 1}"

            headers = [header.text.strip() for header in table.find_all("th")]

            rows = table.find_all("tr")
            data = []
            for row in rows:
                cols = [col.text.strip() for col in row.find_all("td")]
                if cols:
                    data.append(cols)

            subopcao_data["tables"].append({
                "title": title_text,
                "headers": headers,
                "data": data
            })

        all_data.append(subopcao_data)

    return {"ano": ano, "data": all_data}

@app.get("/exportacao")
def get_exportacao(ano: int = Query(2023, description="Ano para filtrar os dados")):
    
    base_url = os.getenv("url_base")
    subopcoes = [f"subopt_0{i}" for i in range(1, 5)]  # subopt_01 a subopt_04
    opcao = "opt_06"

    all_data = []

    for subopcao in subopcoes:
        # Construir a URL dinâmica
        url = f"{base_url}?ano={ano}&opcao={opcao}&subopcao={subopcao}"
        response = requests.get(url)

        if response.status_code != 200:
            all_data.append({"subopcao": subopcao, "error": "Não foi possível acessar o site"})
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", {"class": "tb_base tb_dados"})

        if not tables:
            all_data.append({"subopcao": subopcao, "error": "Nenhuma tabela encontrada"})
            continue

        subopcao_data = {"subopcao": subopcao, "tables": []}
        for table in tables:
            title = table.find_previous("h3") or table.find_previous("h2") or table.find_previous("p")
            title_text = title.text.strip() if title else f"Tabela {len(subopcao_data['tables']) + 1}"

            headers = [header.text.strip() for header in table.find_all("th")]

            rows = table.find_all("tr")
            data = []
            for row in rows:
                cols = [col.text.strip() for col in row.find_all("td")]
                if cols:
                    data.append(cols)

            subopcao_data["tables"].append({
                "title": title_text,
                "headers": headers,
                "data": data
            })

        all_data.append(subopcao_data)

    return {"ano": ano, "data": all_data}
