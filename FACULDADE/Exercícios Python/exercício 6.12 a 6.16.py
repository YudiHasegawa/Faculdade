escolha = float(input("Digite o exercício desejado entre 6.12 6.13 : "))
if escolha == 6.12:
    print("Exercício 6.12")
    L = [1, 7, 2, 4]
    máximo = L[0]
    mínimo = L[0]
    for x in L:
        if x > máximo:
            máximo = x
    print(f"O maior número é {máximo}")
    for y in L:
        if y > máximo:
            mínimo = y
    print(f"O menor número é {mínimo}")
if escolha == 6.13:
    print("Exercício 6.13")
    L = [-10, -8, 0, 1 , 2, 5, -2, -4]
    soma = 0
    máximo = L[0]
    mínimo = L[0]
    for x in L:
        if x > máximo:
            máximo = x
    print(f"O maior número é {máximo}")
    for y in L:
        if y > máximo:
            mínimo = y
    print(f"O menor número é {mínimo}")
    for z in L:
        soma += z
    média = soma / len(L)
    print(f"A média dos números é {média}")