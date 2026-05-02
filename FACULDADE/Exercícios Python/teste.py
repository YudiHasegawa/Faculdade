#Prática de laboratório (minha resolução)
#Tarefa: criar um cadastro simples com dicionário
"""
Requisitos:
Usar dict para armazenar: RA ---> Nome do aluno
Menu: inserir, buscar, listar, remover
Usar .get() e "in" para evitar KeyError
"""
import json
try:
  with open ("dados.json", "r") as arquivo:
    cadastros = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
  cadastros = {}
def novoRA(RAnovo, nome):
  if RAnovo in cadastros:
    return 'Esse RA já está cadastrado'
  cadastros[RAnovo] = nome
  return f"Cadastro realizado: {nome} foi cadastrado com o RA {RAnovo}"
while True:
  try:
    menu = int(input("""
    Olá, seja bem vindo(a)! O que deseja realizar?

    Inserir novo RA (1)
    Buscar RA (2)
    Listar todos os RA (3)
    Remover RA (4)
    Fechar (0)

    """))
  except ValueError:
    print("\nFunção inválida, tente novamente.")
    continue
  if menu == 0:
    print("Fechando...")
    break
  elif menu == 1:
    RAnovo = input("\nDigite o RA ou 0 para voltar: ").strip().lower()
    if RAnovo == "0":
      continue
    nome = input("Digite o nome: ").strip().lower()
    resultado = novoRA(RAnovo, nome)
    print(resultado)
    with open("dados.json", "w") as arquivo:
      json.dump(cadastros, arquivo, indent=4)
  elif menu == 2:
    buscar = input("\nDigite o nome do RA que deseja buscar ou 0 para voltar: ").strip().lower()
    encontrado = False
    if buscar == "0":
      continue
    for ra, nome in cadastros.items():
      if buscar in nome:
        print(f"{ra}: {nome}.")
        encontrado = True
    if not encontrado:
        print("Cadastro não encontrando.")
  elif menu == 3:
    print("")
    for ra, nome in cadastros.items():
      print(f"{ra}: {nome}.")
  elif menu == 4:
    remover = input("\nDigite o RA que deseja remover ou 0 para voltar: ").strip().lower()
    if remover == "0":
      continue
    elif remover in cadastros:
      del cadastros[remover]
      print(f"RA {remover} removido com sucesso")
      with open("dados.json", "w") as arquivo:
        json.dump(cadastros, arquivo, indent=4)
    else:
      print(f"RA não encontrado.")
  else:
    print("\nFunção inválida, tente novamente.")