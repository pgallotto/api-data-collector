# Coleta de Movimentações via API

Este projeto é um script Python que coleta dados de movimentações de uma API e os salva em um arquivo CSV formatado para o padrão brasileiro.

## Funcionalidades

- Coleta dados de uma API paginada.
- Formata valores numéricos para o padrão brasileiro (vírgula como separador decimal).
- Salva os dados em um arquivo CSV.
- Lida com erros de requisição, como limite de requisições (status 429).

## Pré-requisitos

- Python 3.x instalado.
- Bibliotecas listadas no arquivo `requirements.txt`.

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/pgallotto/api-data-collector

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Configure o script:

- Substitua o valor de TOLKEN no cabeçalho da API pelo seu token de autenticação.
- Ajuste os parâmetros datainicial e datafinal conforme necessário.

4. Execute o script:
   ```bash
   python src/coleta_movimentacoes.py

O arquivo CSV será gerado no caminho especificado em CAMINHO_ARQUIVO.
