escolha = float(input("Digite o exercício desejado entre 6.1 6.2 6.3 6.5 6.6 : "))
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
if escolha == 6.2:
    print("Exercício 6.2")
    L1 = []
    L2 = []
    while True:
        item = input("Digite o que deseja adicionar na lista 1 ou digite sair: ")
        if item == ("sair" or "Sair"):
            break
        L1.append(item)
    L3 =  L1[:]
    while True:
        item = input("Digite o que deseja adicionar na lista 2 ou digite sair: ")
        if item == ("sair" or "Sair"):
            break
        L2.append(item)
    L3.extend(L2)
    print(f"""
    Lista 1: {L1}
    Lista 2: {L2}
    Lista 3: {L3}
    """)
if escolha == 6.3:
    print("Exercício 6.3")
    L1 = []
    L2 = []
    while True:
        item = input("Digite o que deseja adicionar na lista 1 ou digite sair: ")
        if item == ("sair" or "Sair"):
            break
        L1.append(item)
    L3 = L1[:]
    while True:
        item = input("Digite o que deseja adicionar na lista 2 ou digite sair: ")
        if item == ("sair" or "Sair"):
            break
        L2.append(item)
    posição = 0
    while posição < len(L2):
        if L2[posição] not in L3:
            L3.append(L2[posição])
        posição += 1
    print(f"""
    Lista 1: {L1}
    Lista 2: {L2}
    Lista 3: {L3}
    """)
if escolha == 6.5:
    print("Exercício 6.5")
    último = 10
    fila = list(range(1, último + 1))
    contador = 0
    while True:
        print(f"""
        Existem {len(fila)} clientes na fila.
        Fila atual: {fila}
        Digite F para adicionar um cliente ao fim da sala .
        Digite A para realizar o atendimento.
        Digite S para sair.
        """)
        operação = input("Operação (F, A ou S): ")
        if "F" in operação:
            contador = operação.count("F")
            while contador > 0:
                último += 1#Incrementa o ticket do novo cliente
                fila.append(último)
                print("Cliente adicionado na fila.")
                contador -= 1
            contador = 0
        if "A" in operação:
            if len(fila) > 0:
                contador = operação.count("A")
                while contador > 0:
                    atendido = fila.pop(0)
                    print(f"Cliente {atendido} atendido.")
                    contador -= 1
                contador = 0
            else:
                print("Fila está vazia! Ninguém para atender.")
        if "S" in operação:
            print("Saindo...")
            break
        if ("A" or "F" or "S") not in operação:
            print("\nOperação inválida Digite apenas F, A ou S!")
if escolha == 6.6:
    print("Exercício 6.6")
    último = 10
    último2 = 10
    fila = list(range(1, último + 1))
    fila2 = list(range(1, último2 + 1))
    contador = 0
    while True:
        print(f"""
        Existem {len(fila)} clientes na fila 1.
        Fila 1 atual: {fila}
        Existem {len(fila2)} clientes na fila 2.
        Fila 2 atual: {fila2}
        Digite F para adicionar um cliente ao fim da sala 1.
        Digite G para adicionar um cliente ao fim da sala 2.
        Digite A para realizar o atendimento da sala 1.
        Digite B para realizar o atendimento da sala 2.
        Digite S para sair.
        """)
        operação = input("Operação (F, G, A, B ou S): ")
        if "F" in operação:
            contador = operação.count("F")
            while contador > 0:
                último += 1#Incrementa o ticket do novo cliente
                fila.append(último)
                print("Cliente adicionado na fila.")
                contador -= 1
            contador = 0
        if "G" in operação:
            contador = operação.count("G")
            while contador > 0:
                último2 += 1#Incrementa o ticket do novo cliente
                fila2.append(último2)
                print("Cliente adicionado na fila 2.")
                contador -= 1
            contador = 0
        if "A" in operação:
            if len(fila) > 0:
                contador = operação.count("A")
                while contador > 0:
                    atendido = fila.pop(0)
                    print(f"Cliente {atendido} da fila 1 atendido.")
                    contador -= 1
                contador = 0
            else:
                print("Fila 1 está vazia! Ninguém para atender.")
        if "B" in operação:
            if len(fila2) > 0:
                contador = operação.count("A")
                while contador > 0:
                    atendido = fila2.pop(0)
                    print(f"Cliente {atendido} da fila 2 atendido.")
                    contador -= 1
                contador = 0
            else:
                print("Fila 2 está vazia! Ninguém para atender.")
        if "S" in operação:
            print("Saindo...")
            break
        if ("A" or "F" or "S"or "G" or "B") not in operação:
            print("\nOperação inválida Digite apenas F, G, A, B ou S!")