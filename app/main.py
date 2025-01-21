from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from app.csvReader import jsonProducao
from app.csvReader import jsonProcessamento
from app.csvReader import jsonComercializacao
from app.csvReader import jsonImportExport

load_dotenv()

app = FastAPI()

@app.get("/producao")
def get_producao(ano: int = Query(2023, description="Ano para filtrar os dados")):

    base_url = os.getenv("url_base")
    opcao = "opt_02"

    url = f"{base_url}?&ano={ano}&opcao={opcao}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro na requisição para PRODUÇÃO: status code {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "tb_base tb_dados"})

    if not table:
        print("Erro ao recuperar dados da tabela. Retornando dados de backup CSV...")
        json_data = jsonProducao("Producao.csv")
        return json_data

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
        print("Erro ao recuperar dados da tabela. Retornando dados de backup CSV...")
        json_data = jsonComercializacao("Comercio.csv")
        return json_data
    
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

    arquivo_mapping = {
        "subopt_01": "ProcessaViniferas.csv",
        "subopt_02": "ProcessaAmericanas.csv",
        "subopt_03": "ProcessaMesa.csv",
        "subopt_04": "ProcessaSemclass.csv"
    }

    all_data = []

    for subopcao in subopcoes:
        # Construir a URL dinâmica
        url = f"{base_url}?ano={ano}&opcao={opcao}&subopcao={subopcao}"
        response = requests.get(url)
            
        if response.status_code != 200:
             #all_data.append({"subopcao": subopcao, "error": "Não foi possível acessar o site"})
            arquivo_backup = arquivo_mapping.get(subopcao)
            if arquivo_backup:
                json_data = jsonProcessamento(arquivo_backup)  # Sua função para ler o CSV
                all_data.append({"subopcao": subopcao, "backup_data": json_data})
            else:
                all_data.append({"subopcao": subopcao, "error": "Arquivo de backup não encontrado"})
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", {"class": "tb_base tb_dados"})

        if not tables:
            arquivo_backup = arquivo_mapping.get(subopcao)
            if arquivo_backup:
                json_data = jsonProcessamento(arquivo_backup)
                all_data.append({"subopcao": subopcao, "backup_data": json_data})
            else:
                all_data.append({"subopcao": subopcao, "error": "Tabela não encontrada e arquivo de backup não disponível"})
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

    arquivo_mapping = {
        "subopt_01": "ImpVinhos.csv",
        "subopt_02": "ImpEspumantes.csv",
        "subopt_03": "ImpPassas.csv",
        "subopt_04": "ImpSuco.csv"
    }

    all_data = []

    for subopcao in subopcoes:
        url = f"{base_url}?ano={ano}&opcao={opcao}&subopcao={subopcao}"
        response = requests.get(url)

        if response.status_code != 200:
            #all_data.append({"subopcao": subopcao, "error": "Não foi possível acessar o site"})
            arquivo_backup = arquivo_mapping.get(subopcao)
            print("Nome arquivo: " +arquivo_backup)
            if arquivo_backup:
                json_data = jsonImportExport(arquivo_backup)  
                all_data.append({"subopcao": subopcao, "backup_data": json_data})
            else:
                all_data.append({"subopcao": subopcao, "error": "Arquivo de backup não encontrado"})
            continue
        

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", {"class": "tb_base tb_dados"})

        if not tables:
            #all_data.append({"subopcao": subopcao, "error": "Nenhuma tabela encontrada"})
            arquivo_backup = arquivo_mapping.get(subopcao)
            if arquivo_backup:
                json_data = jsonImportExport(arquivo_backup)  # Sua função para ler o CSV
                all_data.append({"subopcao": subopcao, "backup_data": json_data})
            else:
                all_data.append({"subopcao": subopcao, "error": "Arquivo de backup não encontrado"})
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
    opcao = "opt_06a"

    arquivo_mapping = {
        "subopt_01": "ImpVinhos.csv",
        "subopt_02": "ImpEspumantes.csv",
        "subopt_03": "ImpPassas.csv",
        "subopt_04": "ImpSuco.csv"
    }

    all_data = []

    for subopcao in subopcoes:
        # Construir a URL dinâmica
        url = f"{base_url}?ano={ano}&opcao={opcao}&subopcao={subopcao}"
        response = requests.get(url)

        if response.status_code != 200:
            all_data.append({"subopcao": subopcao, "error": "Não foi possível acessar o site"})
            arquivo_backup = arquivo_mapping.get(subopcao)
            print("Nome arquivo: " +arquivo_backup)
            if arquivo_backup:
                json_data = jsonImportExport(arquivo_backup)  # Sua função para ler o CSV
                all_data.append({"subopcao": subopcao, "backup_data": json_data})
            else:
                all_data.append({"subopcao": subopcao, "error": "Arquivo de backup não encontrado"})
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", {"class": "tb_base tb_dados"})

        if not tables:
            #all_data.append({"subopcao": subopcao, "error": "Nenhuma tabela encontrada"})
            arquivo_backup = arquivo_mapping.get(subopcao)
            print("Nome arquivo: " +arquivo_backup)
            if arquivo_backup:
                json_data = jsonImportExport(arquivo_backup)  # Sua função para ler o CSV
                all_data.append({"subopcao": subopcao, "backup_data": json_data})
            else:
                all_data.append({"subopcao": subopcao, "error": "Arquivo de backup não encontrado"})
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
