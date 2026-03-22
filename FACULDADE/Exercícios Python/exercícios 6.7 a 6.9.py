escolha = float(input("Digite o exercício desejado entre 6.7 6.8 6.9  : "))
if escolha == 6.7:
    print("Exercício 6.7")
    while True:
        expressão = input("Digite a expressão ou 0 para sair: ")
        pilha = []
        correta = True
        if expressão == "0":
            print("Saindo...")
            break
        for i in range(len(expressão)):
            if expressão[i] == "(":
                pilha.append("(")
            elif expressão[i] == ")":
                if len(pilha) == 0:
                    correta = False
                    break
                pilha.pop()

        if len(pilha) != 0:
            correta = False

        if correta:
            print("Parênteses corretos!")
        else:
            print("Parênteses incorretos!")
if escolha == 6.8:
    print("Exercício 6.8")
    L = [15, 7, 27, 39]
    while True:
        p = int(input("Digite o valor a procurar ou 0 para sair: "))
        posição = 0
        if p == 0:
            print("Saindo...")
            break
        for x in L:
            posição += 1
            if x == p:
                print(f"{p} achado na posição {posição}.")
                break
        else:
            print(f"{p} não encontrando.")
if escolha == 6.9:
    print("Exercício 6.9")
    L = [15, 7, 27, 39]
    while True:
        p = int(input("Digite o primeiro valor a procurar ou 0 para sair: "))
        v = int(input("Digite o segundo valor a procurar: "))
        posição = 0
        posição2 = 0
        if p == 0:
            print("Saindo...")
            break
        achou = True
        for x in L:
            posição += 1
            if x == p:
                print(f"{p} achado na posição {posição}.")
                break
        else:
            print(f"{p} não encontrando.")
        for x in L:
            if x == v:
                print(f"{v} achado na posição {posição2}.")
                break
        else:
            print(f"{v} não encontrando.")
        