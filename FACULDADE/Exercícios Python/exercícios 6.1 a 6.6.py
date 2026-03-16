escolha = float(input("Digite o exercício desejado entre 6.1 6.2 6.3 6.4 6.5 6.6 : "))
if escolha == 6.1:
    print("Exercício 6.1")
    notas = [0, 0, 0, 0, 0, 0, 0]
    contador = 0
    soma = 0
    while contador < 7:
        notas[contador] = float(input(f"Digite a {contador + 1} nota: "))
        soma += notas[contador]
        contador += 1
    contador = 0
    while contador < 7:
        print(f"Nota {contador + 1}: {notas[contador]}.")
        contador += 1
    print(f"A média das notas é {soma / contador:.2f}.")
