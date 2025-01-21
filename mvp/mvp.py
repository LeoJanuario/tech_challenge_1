import requests
import time
import subprocess

URL = "http://127.0.0.1:8000/"
def menu():
    print("\n--- Aplicativo Cliente para Tech Challenge API ---")
    print("1. Consultar Produção")
    print("2. Consultar Processamento")
    print("3. Consultar Comercialização")
    print("4. Consultar Importação")
    print("5. Consultar Exportação")
    print("6. Sair")

def consultar(endpoint):
    try:
        url = f"{URL}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            print("\n---------- Resultado ----------")
            print(response.json())
        else:
            print(f"\nErro: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as error:
        print(f"\nErro na conexão com a API: {error}")

def start_server():
    command = ["uvicorn", "app.main:app", "--reload"]
    process = subprocess.Popen(command)
    return process

def main():
    process = start_server()
    
    print("Iniciando servidor local...")
    time.sleep(5)
    
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            consultar("producao")
        elif opcao == "2":
            consultar("processamento")
        elif opcao == "3":
            consultar("comercializacao")
        elif opcao == "4":
            consultar("importacao")
        elif opcao == "5":
            consultar("exportacao")
        elif opcao == "6":
            print("Saindo...")
            process.terminate()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()