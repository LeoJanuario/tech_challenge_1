from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import pandas as pd  # Importar pandas

app = FastAPI()

@app.get("/dados")
def get_dados():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
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

# Para testar localmente, chame a função diretamente:
if __name__ == "__main__":
    # Chama a função e armazena o retorno
    response = get_dados()

    # Verifica se não há erros no retorno
    if "error" not in response:
        # Cria um DataFrame com os dados
        df = pd.DataFrame(response["data"], columns=response["headers"])
        print(df)
    else:
        print(response["error"])
