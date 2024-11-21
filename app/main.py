from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/dados")
def get_dados():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02" 
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Não foi possível acessar o site"}

    # Parse do HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encontra a tabela específica pela classe
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Tabela não encontrada"}

    # Extrair cabeçalhos da tabela
    headers = [header.text.strip() for header in table.find_all("th")]

    # Extrair as linhas de dados
    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = [col.text.strip() for col in row.find_all("td")]
        if cols:  # Adicionar apenas se a linha tiver colunas (evitar cabeçalhos vazios)
            data.append(cols)

    return {
        "headers": headers,
        "data": data
    }


