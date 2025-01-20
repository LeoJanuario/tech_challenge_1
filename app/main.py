from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from app.csvReader import jsonProducao

load_dotenv()

app = FastAPI()

### Rota para retornar dados da aba de produção no siti VitiBrasil
@app.get("/producao")
def get_producao():

    url = os.getenv("url_producao")
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Não foi possível acessar o site"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        print("------------->Erro na requisição: Tabela não encontrada")  # Adicionando o print
        #return {"error": "Tabela não encontrada"}
        json_data = jsonProducao("Producao.csv")
        #print("Valor" + str(json_data))
        #return json_data

    
    headers = [header.text.strip() for header in table.find_all("th")]

    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = [col.text.strip() for col in row.find_all("td")]
        if cols:
            data.append(cols)

    return {
        "headers": headers,
        "data": data
    }

@app.get("/comercializacao")
def get_comercializacao():
    url = os.getenv("url_comercializacao")
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
        "headers": headers,
        "data": data
    }

@app.get("/processamento")
def get_processamento():
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"
    subopcoes = [f"subopt_0{i}" for i in range(1, 5)]  # subopt_01 a subopt_04
    opcao = "opt_03"

    all_data = []

    for subopcao in subopcoes:
        # Construir a URL dinâmica
        url = f"{base_url}?subopcao={subopcao}&opcao={opcao}"
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

    return all_data


@app.get("/importacao")
def get_importacao():
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"
    subopcoes = [f"subopt_0{i}" for i in range(1, 6)]  # subopt_01 a subopt_04
    opcao = "opt_05"

    all_data = []

    for subopcao in subopcoes:
        url = f"{base_url}?subopcao={subopcao}&opcao={opcao}"
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

    return all_data

@app.get("/exportacao")
def get_exportacao():
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"
    subopcoes = [f"subopt_0{i}" for i in range(1, 5)]  # subopt_01 a subopt_04
    opcao = "opt_06"

    all_data = []

    for subopcao in subopcoes:
        url = f"{base_url}?subopcao={subopcao}&opcao={opcao}"
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

    return all_data
