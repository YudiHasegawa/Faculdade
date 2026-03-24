escolha = float(input("Digite o exercício desejado entre 6.12 6.13 6.16 : "))
if escolha == 6.12:
    print("Exercício 6.12")
    #Faça um programa que mostre o menor elemento de uma lista
    L = []
    while True:
        elemento = int(input("Digite um número inteiro para adicionar na lista ou apertar 0 para sair: "))
        L.append(elemento)
        if elemento == 0:
            break
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
if escolha == 6.16:
    print("Exercício 6.16")
    L = [7, 4, 3, 12, 8]
    fim = 5
    while fim > 1:
        trocou = False
        x = 0
        while x < (fim - 1):
            if L[x] < L[x + 1]:
                trocou = True
                temp = L[x]
                L[x] = L[x + 1]
                L[x + 1] = temp
            x += 1
        if not trocou:
            break
        fim -= 1
    for e in L:
        print(e)
