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

camisetas = {"CAMISETA BOXY HEAVYWEIGHT": {"Preço": 149.90, 
                                           "Quantidade": 45,
                                           "Gramatura": 260},
             "CAMISETA OVERSIZED VINTAGE WASH": {"Preço": 129.00,
                                                 "Quantidade": 30,
                                                 "Gramatura": 220}}
calças = {"CALÇA WIDE LEG CANVAS": {"Preço": 259.00,
                                    "Quantidade": 15,
                                    "Gramatura": 380},
          "CALÇA CARGO PARACHUTE PANTS": {"Preço": 239.90,
                                          "Quantidade": 8,
                                          "Gramatura": 180}}
blusas = {"BLUSA HODDIE DROP SHOULDER": {"Preço": 289.00,
                                         "Quantidade": 12,
                                         "Gramatura": 450},
          "BLUSA CREWNECK MINIMALIST": {"Preço": 219.00,
                                        "Quantidade": 20,
                                        "Gramatura": 400}}
def venda (escolha, quantidade, menu):
  if quantidade <= menu[escolha][("Quantidade")]:
    preçototal = quantidade * menu[escolha][("Preço")]
    menu[escolha].update({("Quantidade"): menu[escolha][("Quantidade")] - quantidade})
    return f"\nO preço total será de: {preçototal:.2f}.\n"
  else:
    return "\nDigite uma quantidade válida.\n"
while True:
  print("=" * 40)
  menu = input(f"""Bem-vindo(a) a loja de roupas caras pra caralho!!! :O

  1 - Camisetas
  2 - Calças
  3 - Blusas
  4 - Sair
  Escreva a opção desejada: """).strip().lower()
  print("=" * 40)
  if menu == "sair" or menu == "4":
    break
  elif menu == "camisetas" or menu == "1":
    opção = camisetas
    while True:
      for roupa, estoque in camisetas.items():
        print(f"{roupa}")
        for chave, numero in estoque.items():
          print(f"{chave}: {numero}")
        print("=" * 40)
      escolha = input("Digite a peça desejada ou digite S para sair: ").strip().upper()
      if escolha == "S":
        print("")
        break
      elif escolha == "CAMISETA BOXY HEAVYWEIGHT":
        if camisetas["CAMISETA BOXY HEAVYWEIGHT"]["Quantidade"] > 0:
          try:
            quantidade = int(input("Digite a quantidade desejada ou 0 para sair: "))
            if quantidade == 0:
              print("")
              break
            retornar = venda(escolha, quantidade, opção)
            print(retornar)
          except ValueError:
            print("\nDigite uma quantidade válida.\n")
            continue
        else:
            print("\nO estoque desta camiseta acabou!!!\n")
      elif escolha == "CAMISETA OVERSIZED VINTAGE WASH":
        if camisetas["CAMISETA OVERSIZED VINTAGE WASH"]["Quantidade"] > 0:
          try:
            quantidade = int(input("Digite a quantidade desejada ou 0 para sair: "))
            if quantidade == 0:
              print("")
              break
            retornar = venda(escolha, quantidade, opção)
            print(retornar)
          except ValueError:
            print("\nDigite uma quantidade válida.\n")
            continue
        else:
            print("\nO estoque desta camiseta acabou!!!\n")
      break
  elif menu == "calças" or menu == "2":
    opção = calças
    while True:
      for roupa, estoque in calças.items():
        print(f"{roupa}")
        for chave, numero in estoque.items():
          print(f"{chave}: {numero}")
        print("=" * 40)
      escolha = input("Digite a peça desejada ou digite S para sair: ").strip().upper()
      if escolha == "S":
        print("")
        break
      elif escolha == "CALÇA WIDE LEG CANVAS":
        if calças["CALÇA WIDE LEG CANVAS"]["Quantidade"] > 0:
          try:
            quantidade = int(input("Digite a quantidade desejada ou 0 para sair: "))
            if quantidade == 0:
              print("")
              break
            retornar = venda(escolha, quantidade, opção)
            print(retornar)
          except ValueError:
            print("\nDigite uma quantidade válida.\n")
            continue
        else:
            print("\nO estoque desta camiseta acabou!!!\n")
      elif escolha == "CALÇA CARGO PARACHUTE PANTS":
        if calças["CALÇA CARGO PARACHUTE PANTS"]["Quantidade"] > 0:
          try:
            quantidade = int(input("Digite a quantidade desejada ou 0 para sair: "))
            if quantidade == 0:
              print("")
              break
            retornar = venda(escolha, quantidade, opção)
            print(retornar)
          except ValueError:
            print("\nDigite uma quantidade válida.\n")
            continue
        else:
            print("\nO estoque desta camiseta acabou!!!\n")
      break
  elif menu == "blusas" or menu == "3":
    opção = blusas
    while True:
      for roupa, estoque in blusas.items():
        print(f"{roupa}")
        for chave, numero in estoque.items():
          print(f"{chave}: {numero}")
        print("=" * 40)
      escolha = input("Digite a peça desejada ou digite S para sair: ").strip().upper()
      if escolha == "S":
        print("")
        break
      elif escolha == "BLUSA HODDIE DROP SHOULDER":
        if blusas["BLUSA HODDIE DROP SHOULDER"]["Quantidade"] > 0:
          try:
            quantidade = int(input("Digite a quantidade desejada ou 0 para sair: "))
            if quantidade == 0:
              print("")
              break
            retornar = venda(escolha, quantidade, opção)
            print(retornar)
          except ValueError:
            print("\nDigite uma quantidade válida.\n")
            continue
        else:
            print("\nO estoque desta camiseta acabou!!!\n")
      elif escolha == "BLUSA CREWNECK MINIMALIST":
        if blusas["BLUSA CREWNECK MINIMALIST"]["Quantidade"] > 0:
          try:
            quantidade = int(input("Digite a quantidade desejada ou 0 para sair: "))
            if quantidade == 0:
              print("")
              break
            retornar = venda(escolha, quantidade, opção)
            print(retornar)
          except ValueError:
            print("\nDigite uma quantidade válida.\n")
            continue
        else:
            print("\nO estoque desta camiseta acabou!!!\n")
      break
  else:
    print("\nDigite uma opção válida.\n")