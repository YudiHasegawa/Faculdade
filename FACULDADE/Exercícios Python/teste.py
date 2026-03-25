lista = {}
todos = 0
while True:
    nome = input("\nDigite o item que você comprou ou 0 para sair: ")
    if nome == "0":
        break
    quantidade = int(input("Digite a quantidade que comprou: "))
    custo = float(input("Digite o preço do individual do item: "))
    valor_final = quantidade * custo
    lista[f"{nome}"] = [quantidade, custo, valor_final]
    todos += lista[f"{nome}"][1]
print("\nAqui está a tabela de gastos (item, quantidade, custo invidivual e custo total\n")
for e in lista:
    print(lista[f"{e}"])
