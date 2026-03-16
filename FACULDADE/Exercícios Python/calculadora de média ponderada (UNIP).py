#Calculadora de média ponderada entre 3 números
#Baseado no sistema de notas da UNIP
#NP1 - peso 4 / NP2 - peso 4 / PIM = peso 2
notas = [0, 0, 0]
pesos = [0, 0, 0]
contadornota = 0
contadorsoma = 0
soma = 0
somapeso = 0
while contadornota < 3 and contadorsoma < 3:
    notas[contadornota] = float(input(f"Digite a {contadornota + 1} nota: "))
    pesos[contadorsoma] = float(input(f"Digite o peso da nota: "))
    soma += (notas[contadornota] * pesos[contadorsoma])
    somapeso += pesos[contadorsoma]
    contadornota += 1
    contadorsoma += 1
contadornota = 0
contadorsoma = 0
while contadornota < 3 and contadorsoma < 3:
    print(f"Nota {contadornota + 1}: {notas[contadornota]}.")
    print(f"Peso {contadorsoma + 1}: {pesos[contadorsoma]}.")
    contadornota += 1
    contadorsoma += 1
print(f"A média das notas é {soma / somapeso:.2f}.")
