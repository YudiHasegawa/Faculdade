lista = {}
todos = 0
while True:
    nome = input("\nDigite o item que você comprou ou 0 para sair: ")
    if nome == "0":
        break
    quantidade = int(input("Digite a quantidade que comprou: "))
    custo = float(input("Digite o preço do individual do item: "))
    valor_total = quantidade * custo
    lista[nome] = {
        "quantidade": quantidade,
        "custo": custo,
        "valor_total": valor_total}
    todos += valor_total
print("\nAqui está a tabela de gastos (item, quantidade e custo total\n")
for nome, dados in lista.items():
    print(f"{nome} - Quantidade: {dados["quantidade"]} - Total: R${dados["valor_total"]}")