#Crie um programa que gerencia o estoque de uma loja
'''
Requisitos: Use um Dicionário de Dicionários. 
A chave principal é o tipo de roupa
As chaves dentro da principal são as opções desse tipo de roupa (ex: "CAMISETA BOXY HEAVYWEIGHT"). 
O valor é outro dicionário contendo preço, quantidade e gramatura.

O programa deve permitir atualizar o estoque. Se a quantidade chegar a 0, 
deve disparar uma Exception customizada (ou um erro tratado) avisando que o item 
está esgotado.
'''
import json
arquivo = "estoque.json"
def carregar_estoque():
  try:
    with open ("estoque.json", "r") as f:
      return json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    return {
      "camisetas": {"CAMISETA BOXY HEAVYWEIGHT": {"Preço": 149.90, 
                                                "Quantidade": 45,
                                                "Gramatura": 260},
                  "CAMISETA OVERSIZED VINTAGE WASH": {"Preço": 129.00,
                                                      "Quantidade": 30,
                                                      "Gramatura": 220}},
      "calças": {"CALÇA WIDE LEG CANVAS": {"Preço": 259.00,
                                          "Quantidade": 15,
                                          "Gramatura": 380},
                "CALÇA CARGO PARACHUTE PANTS": {"Preço": 239.90,
                                                "Quantidade": 8,
                                                "Gramatura": 180}},
      "blusas": {"BLUSA HODDIE DROP SHOULDER": {"Preço": 289.00,
                                              "Quantidade": 12,
                                              "Gramatura": 450},
                "BLUSA CREWNECK MINIMALIST": {"Preço": 219.00,
                                              "Quantidade": 20,
                                              "Gramatura": 400}}
            }
estoque_geral = carregar_estoque()
def salvar_estoque(dados):
  with open(arquivo, "w") as f:
    json.dump(dados, f, indent=4)
def venda (categoria, produto, quantidade, estoque_geral):
    item = estoque_geral[categoria][produto]
    if quantidade <= item["Quantidade"]:
      valor = quantidade * item["Preço"]
      item["Quantidade"] -= quantidade
      salvar_estoque(estoque_geral)
      return f"\nO preço total será de: R$ {valor:.2f}.\n"
    return "\nDigite uma quantidade válida.\n"
categoria_menu = {"1": "camisetas", "camisetas": "camisetas", "camiseta": "camisetas",
                  "2": "calças", "calças": "calças", "calça": "calças",
                  "3": "blusas", "blusas": "blusas", "blusa": "blusas"}
while True:
    print("=" * 40)
    menu = input(f"""Bem-vindo(a) a loja de roupas caras pra caralho!!! :O

    1 - Camisetas
    2 - Calças
    3 - Blusas
    4 - Sair
    Escreva a opção desejada: """).strip().lower()
    print("=" * 40)
    if menu in ["4", "sair"]:
      print("Saindo...")
      break
    elif menu not in categoria_menu:
      print("Digite uma opção válida.")
      continue
    categoria_nome = categoria_menu[menu]
    itens = estoque_geral[categoria_nome]
    for roupa, estoque in itens.items():
        print(f"{roupa}")
        for chave, numero in estoque.items():
          print(f"{chave}: {numero}")
        print("=" * 40)
    escolha = input("Digite a peça desejada ou digite S para sair: ").strip().upper()