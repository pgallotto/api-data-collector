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
   git clone https://github.com/seu-usuario/coleta-movimentacoes-api.git
