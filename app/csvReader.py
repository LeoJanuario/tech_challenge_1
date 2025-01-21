import pandas as pd
import math

def jsonProducao(nome_arquivo):

    caminho_completo = "csvs\\" + nome_arquivo
    airbnb_data = pd.read_csv(caminho_completo, sep=';')

    dados = airbnb_data.to_dict(orient='records')
    
    resultado = {
        "headers": ["Produto", "Quantidade (L.)"],
        "data": []
    }

    anos = set()

    for produto in dados:
        for ano in produto.keys():
            if ano.isdigit():
                anos.add(int(ano))

    ano_inicial = min(anos)
    ano_final = max(anos)

    for produto in dados:
        nome_produto = produto["produto"]
        quantidade_total = 0
        
        for ano in range(ano_inicial, ano_final + 1):
            quantidade_total += produto.get(str(ano), 0)
        
        quantidade_formatada = f"{quantidade_total:,}".replace(",", ".")
        
        resultado["data"].append([nome_produto, quantidade_formatada])

    return resultado

def jsonProcessamento(nome_arquivo):

    caminho_completo = "csvs\\" + nome_arquivo
    airbnb_data = pd.read_csv(caminho_completo, sep=';')

    dados = airbnb_data.to_dict(orient='records')
    
    resultado = {
        "headers": ["Cultivar", "Quantidade (L.)"],
        "data": []
    }

    anos = set()

    for cultivar in dados:
        for ano in cultivar.keys():
            if ano.isdigit():
                anos.add(int(ano))

    ano_inicial = min(anos)
    ano_final = max(anos)

    for cultivar in dados:
        nome_cultivar = cultivar.get("cultivar", "")
        if isinstance(nome_cultivar, str):
            nome_cultivar = nome_cultivar.strip()
        else:
            nome_cultivar = "" 
        if not nome_cultivar:
            continue
        
        quantidade_total = 0
        
        for ano in range(ano_inicial, ano_final + 1):
            try:
                quantidade = float(cultivar.get(str(ano), 0))
                if math.isnan(quantidade):
                    quantidade = 0
                quantidade_total += quantidade
            except (ValueError, TypeError):
                quantidade_total += 0
        
        quantidade_formatada = f"{quantidade_total:,.1f}".replace(",", ".")
        
        resultado["data"].append([nome_cultivar, quantidade_formatada])

    for i, item in enumerate(resultado["data"]):
        if item[0] is None or item[1] == "NaN" or item[1] == "0.0":
            resultado["data"].pop(i)
    
    return resultado

def jsonComercializacao(nome_arquivo):
    
    caminho_completo = "csvs\\" + nome_arquivo
    airbnb_data = pd.read_csv(caminho_completo, sep=';')
    dados = airbnb_data.to_dict(orient='records')
    
    resultado = {
        "headers": ["Produto", "Quantidade (L.)"],
        "data": []
    }

    anos = set()

    for produto in dados:
        for ano in produto.keys():
            if ano.isdigit(): 
                anos.add(int(ano))

    ano_inicial = min(anos)
    ano_final = max(anos)

    for produto in dados:
        nome_produto = produto["Produto"]
        quantidade_total = 0
        
        for ano in range(ano_inicial, ano_final + 1):
            quantidade_total += produto.get(str(ano), 0) 
        
        quantidade_formatada = f"{quantidade_total:,}".replace(",", ".")
        resultado["data"].append([nome_produto, quantidade_formatada])

    return resultado


def jsonImportExport(nome_arquivo):

    caminho_completo = "csvs\\" + nome_arquivo

    encodings = ['utf-8', 'ISO-8859-1', 'latin1']
    airbnb_data = None
    for encoding in encodings:
        try:
            airbnb_data = pd.read_csv(caminho_completo, sep=';', encoding=encoding)
            break
        except UnicodeDecodeError as e:
            print(f"Erro ao tentar ler com a codificação {encoding}: {e}")
        except Exception as e:
            print(f"Erro inesperado ao tentar ler o arquivo: {e}")
    
    if airbnb_data is None:
        raise ValueError(f"Não foi possível ler o arquivo com as codificações tentadas: {encodings}")

    dados = airbnb_data.to_dict(orient='records')
    
    resultado = {
        "headers": ["País", "Quantidade (L.)"],
        "data": []
    }

    anos = set()

    for pais in dados:  
        for ano in pais.keys():  
            if ano.isdigit(): 
                anos.add(int(ano)) 

    ano_inicial = min(anos)
    ano_final = max(anos)

    for pais in dados:
        nome_pais = pais.get("País", "")
        if isinstance(nome_pais, str):
            nome_pais = nome_pais.strip()
        else:
            nome_pais = "" 
        
        if not nome_pais:
            continue
        
        quantidade_total = 0
        
        for ano in range(ano_inicial, ano_final + 1):
            try:
                quantidade = float(pais.get(str(ano), 0)) 

                if math.isnan(quantidade):
                    quantidade = 0
                quantidade_total += quantidade
            except (ValueError, TypeError):
                quantidade_total += 0 
        
        quantidade_formatada = f"{quantidade_total:,.1f}".replace(",", ".")
        
        resultado["data"].append([nome_pais, quantidade_formatada])

    for i, item in enumerate(resultado["data"]):
        if item[0] is None or item[1] == "NaN" or item[1] == "0.0":
            resultado["data"].pop(i)
    
    return resultado