import pandas as pd
import math

def jsonProducao(nome_arquivo):
    # Caminho completo do arquivo CSV
    caminho_completo = "csvs\\" + nome_arquivo
    
    # Carregar o CSV com pandas
    airbnb_data = pd.read_csv(caminho_completo, sep=';')

    # Converter o DataFrame diretamente para uma lista de dicionários
    dados = airbnb_data.to_dict(orient='records')
    
    # Inicializar a estrutura final
    resultado = {
        "headers": ["Produto", "Quantidade (L.)"],
        "data": []
    }

    # Determinar o menor e maior ano automaticamente
    anos = set()  # Usaremos um set para armazenar todos os anos encontrados

    # Percorrer todos os produtos e coletar todos os anos
    for produto in dados:
        for ano in produto.keys():
            if ano.isdigit():  # Verifica se a chave é um ano (com 4 dígitos)
                anos.add(int(ano))  # Adiciona o ano ao set

    # Identificar o menor e maior ano
    ano_inicial = min(anos)
    ano_final = max(anos)

    # Iterando sobre os produtos e somando as quantidades de cada ano
    for produto in dados:
        nome_produto = produto["produto"]
        quantidade_total = 0
        
        # Somando os valores para todos os anos identificados (entre ano_inicial e ano_final)
        for ano in range(ano_inicial, ano_final + 1):  # Incluindo o ano_final
            quantidade_total += produto.get(str(ano), 0)  # Evita erros se o ano não estiver presente
        
        # Formatando a quantidade total para o formato desejado (com pontos para separação de milhar)
        quantidade_formatada = f"{quantidade_total:,}".replace(",", ".")
        
        # Adicionando os dados ao resultado
        resultado["data"].append([nome_produto, quantidade_formatada])

    # Retornar o resultado em formato JSON sem quebras de linha (ideal para web)
    #return json.dumps(resultado, indent=None, separators=(',', ':'), ensure_ascii=False)
    return resultado

def jsonProcessamento(nome_arquivo):
    # Caminho completo do arquivo CSV
    caminho_completo = "csvs\\" + nome_arquivo
    
    # Carregar o CSV com pandas
    airbnb_data = pd.read_csv(caminho_completo, sep=';')

    # Converter o DataFrame diretamente para uma lista de dicionários
    dados = airbnb_data.to_dict(orient='records')
    
    # Inicializar a estrutura final
    resultado = {
        "headers": ["Cultivar", "Quantidade (L.)"],  # Alterado "Produto" para "Cultivar"
        "data": []
    }

    # Determinar o menor e maior ano automaticamente
    anos = set()  # Usaremos um set para armazenar todos os anos encontrados

    # Percorrer todos os produtos e coletar todos os anos
    for cultivar in dados:  # Alterado "produto" para "cultivar"
        for ano in cultivar.keys():  # Alterado "produto" para "cultivar"
            if ano.isdigit():  # Verifica se a chave é um ano (com 4 dígitos)
                anos.add(int(ano))  # Adiciona o ano ao set

    # Identificar o menor e maior ano
    ano_inicial = min(anos)
    ano_final = max(anos)

    # Iterando sobre os produtos e somando as quantidades de cada ano
    for cultivar in dados:  # Alterado "produto" para "cultivar"
        nome_cultivar = cultivar.get("cultivar", "")
        if isinstance(nome_cultivar, str):  # Verifica se o valor é uma string
            nome_cultivar = nome_cultivar.strip()  # Garantir que não tenha espaços extras
        else:
            nome_cultivar = ""  # Se não for string, atribui uma string vazia
        
        if not nome_cultivar:  # Ignorar se o nome do cultivar for vazio ou NaN
            continue
        
        quantidade_total = 0
        
        # Somando os valores para todos os anos identificados (entre ano_inicial e ano_final)
        for ano in range(ano_inicial, ano_final + 1):  # Incluindo o ano_final
            # Tentando converter os valores para float, se falhar, usa 0
            try:
                quantidade = float(cultivar.get(str(ano), 0))  # Converte para float
                # Verifica se a quantidade é um valor 'nan' e substitui por 0
                if math.isnan(quantidade):
                    quantidade = 0
                quantidade_total += quantidade
            except (ValueError, TypeError):
                quantidade_total += 0  # Se a conversão falhar ou o valor for inválido, assume 0
        
        # Formatando a quantidade total para o formato desejado (com pontos para separação de milhar)
        quantidade_formatada = f"{quantidade_total:,.1f}".replace(",", ".")
        
        # Adicionando os dados ao resultado
        resultado["data"].append([nome_cultivar, quantidade_formatada])  # Alterado "produto" para "cultivar"

    # Limpeza de valores NaN no resultado
    for i, item in enumerate(resultado["data"]):
        if item[0] is None or item[1] == "NaN" or item[1] == "0.0":
            resultado["data"].pop(i)
    
    return resultado  # Retorna o dicionário limpo (sem 'NaN' ou valores indesejados)