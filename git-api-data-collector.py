import requests
import csv
import os
import time

# Configurações da API
URL = "https://api.sagierp.com.br/api/v1/movimentos"
PARAMS = {
    "datainicial": "2025-01-01",
    "datafinal": "2025-02-24",
    "limit": 100,  
    "offset": 1  
}
HEADERS = {
    "Authorization": "Bearer TOLKEN",
    "Accept": "application/json"
}

# Diretório e nome do arquivo CSV
CAMINHO_PASTA = r"C:\\Users\\ADM_COMPRAS\\Documents\\python\\Compras"
CAMINHO_ARQUIVO = os.path.join(CAMINHO_PASTA, "movimentacoes.csv")


def formatar_numeros(dados):
    """ Formata os valores numéricos para o padrão brasileiro. """
    for item in dados:
        for chave in ["peso_bruto", "peso_tara", "peso_liquido", "desconto", "preco", "valor_total"]:
            if chave in item and isinstance(item[chave], (int, float)):
                item[chave] = str(item[chave]).replace(".", ",")
    return dados


def coletar_dados():
    """ Coleta os dados da API e armazena em uma lista. """
    todos_os_dados = []
    pagina = 1

    while True:
        print(f"📡 Solicitando dados da página {pagina}...")
        response = requests.get(URL, params=PARAMS, headers=HEADERS)

        if response.status_code == 200:
            dados = response.json()
            if isinstance(dados, dict) and "results" in dados and isinstance(dados["results"], list) and dados["results"]:
                todos_os_dados.extend(dados["results"])
                PARAMS["offset"] += 1
                pagina += 1
                time.sleep(1)
            else:
                print("✅ Nenhum dado encontrado ou fim das páginas.")
                break
        elif response.status_code == 429:
            print("⚠️ Muitas requisições! Esperando 60 segundos antes de continuar...")
            time.sleep(60)
        else:
            print(f"❌ Erro na requisição: {response.status_code}")
            print("📝 Detalhes:", response.text)
            break

    return todos_os_dados


def salvar_csv(dados):
    """ Salva os dados coletados em um arquivo CSV. """
    if not dados:
        print("⚠️ Nenhuma movimentação foi coletada.")
        return
    
    if not os.path.exists(CAMINHO_PASTA):
        os.makedirs(CAMINHO_PASTA)
    
    colunas = list(dados[0].keys())
    
    try:
        with open(CAMINHO_ARQUIVO, mode="w", newline="", encoding="utf-8-sig") as arquivo_csv:
            escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=";")
            escritor.writeheader()
            escritor.writerows(formatar_numeros(dados))
        print(f"✅ Arquivo CSV criado com sucesso em: {CAMINHO_ARQUIVO}")
    except Exception as e:
        print(f"❌ Erro ao criar o arquivo CSV: {e}")


def main():
    """ Função principal para rodar o script. """
    dados = coletar_dados()
    salvar_csv(dados)
    print("🚀 Coleta de dados finalizada!")


if __name__ == "__main__":
    main()