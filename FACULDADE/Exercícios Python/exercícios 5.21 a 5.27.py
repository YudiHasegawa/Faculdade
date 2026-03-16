escolha = float(input("Digite o exercício desejado entre 5.21 5.22 5.23 5.24 5.25 5.26 5.27: "))
if escolha == 5.21:
    print("Exercício 5.21")
    #Faça um programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor
    #Deve contar as cédulas: 100, 50, 20, 10, 5, 1, 0.50, 0.10, 0.05, 0.02, 0.01, 0.001
    while True:
        valor = float(input("Digite o valor a pagar: "))
        if valor == 0:
            print("Programa finalizado.")
            break
        cédulas = 0
        atual = 100
        apagar = valor
        while True:
            if atual <= apagar:
                apagar -= atual
                cédulas += 1
            else:
                print(f"{cédulas} cédula(s) de R$ {atual}")
                if apagar < 0.001:
                    break
                if atual == 100:
                    atual = 50
                elif atual == 50:
                    atual = 20
                elif atual == 20:
                    atual = 10
                elif atual == 10:
                    atual = 5
                elif atual == 5:
                    atual = 1
                elif atual == 1:
                    atual = 0.5
                elif atual == 0.5:
                    atual = 0.2
                elif atual == 0.2:
                    atual = 0.1
                elif atual == 0.1:
                    atual = 0.05
                elif atual == 0.05:
                    atual = 0.02
                elif atual == 0.02:
                    atual = 0.01
                elif atual == 0.01:
                    atual = 0.001
                cédulas = 0
if escolha == 5.22:
    print("Exercício 5.22")
    #Faça um programa que exiba uma lista de opções(menu): adição, subtração, divisão, multiplicação e sair.
    #Imprima a tabuada 1 até a 10 da operação escolhida. Repita até que a opção saída seja escolhida
    while True:
        opção = input("""
        Menu
        
        Escolha uma das seguintes opções:
        Adição
        Subtração
        Multiplicação
        Divisão
        Finalizar
                      
        : """)
        contador = 1
        if opção.lower() not in ("adição", "subtração", "multiplicação", "divisão", "finalizar"):
            print("Digite uma opção válida.")
        if opção.lower() == "finalizar":
             break
        if opção.lower() == "adição":
                while contador == 1:
                    tabuada = 1
                    while tabuada <= 10:
                        número = 1
                        while número <= 10:
                                print(f"{tabuada} + {número} = {tabuada + número}")
                                número += 1
                        tabuada += 1
                        if tabuada > 10:
                            contador = 0
        elif opção.lower() == "subtração":
                while contador == 1:
                    tabuada = 1
                    while tabuada <= 10:
                        número = 1
                        while número <= 10:
                                print(f"{tabuada} - {número} = {tabuada - número}")
                                número += 1
                        tabuada += 1
                        if tabuada > 10:
                            contador = 0
        elif opção.lower() == "multiplicação":
                while contador == 1:
                    tabuada = 1
                    while tabuada <= 10:
                        número = 1
                        while número <= 10:
                                print(f"{tabuada} x {número} = {tabuada * número}")
                                número += 1
                        tabuada += 1
                        if tabuada > 10:
                            contador = 0
        elif opção.lower() == "divisão":
                while contador == 1:
                    tabuada = 1
                    while tabuada <= 10:
                        número = 1
                        while número <= 10:
                                print(f"{tabuada} : {número} = {tabuada / número}")
                                número += 1
                        tabuada += 1
                        if tabuada > 10:
                            contador = 0
if escolha == 5.23:
    normaloubonus = int(input("Exercício 5.23 normal (1) ou bônus (2)?: "))
    if normaloubonus == 1:
        num = int(input("Digite um número para saber se é número primo ou não: "))    
        divisor = 1
        contador = 0
        while divisor <= num:
            resultado = num / divisor
            divisor += 1
            if resultado.is_integer():
                resultado = int(resultado)
            if isinstance(resultado, int):
                contador += 1
        if contador == 2:
            print(f"O número {num} é número primo.")
        else:
            print(f"O número {num} não número primo é primo.")
    if normaloubonus == 2:
        print("Bônus")
        num = int(input("Digite um número para saber se é número primo ou não: "))
        contador = 0
        divisor = 1
        while divisor <= num:
            if num % divisor == 0:
                contador += 1
            divisor += 1
        if contador == 2:
            print(f"O número {num} é número primo.")
        else:
            print(f"O número {num} não é número primo.")
if escolha == 5.24:
    print("Exercício 5.24")
    nummax = int(input("Digite o número máximo que deseja: "))
    num = 2
    total = 0
    while num <= nummax:
        contador = 0
        divisor = 1
        while divisor <= nummax:
            if num % divisor == 0:
                contador += 1
            divisor += 1
        if contador == 2:
            print(f"O número {num} é número primo.")
            total += 1
        num += 1
    if num > nummax:
         print(f"O total de números primos é {total}.")
if escolha == 5.25:
    print("Exercício 5.25")
    num = int(input("Digite o número para calcular a raiz quadrada: "))
    dedutor = num / 2
    diferença = 1
    while diferença > 0.0001:
        dedutornovo = (dedutor + num / dedutor) / 2
        diferença = abs(dedutornovo - dedutor)
        dedutor = dedutornovo
    print(f"A raiz quadrada de {num} é de aproximadamente {dedutornovo:.2f}")
if escolha == 5.26:
    print("Exercício 2.26")
    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))
    sobra = num_1
    while sobra >= num_2:
        sobranova = sobra - num_2
        sobra = sobranova
    else:
        print(f"O resultado da sobra da divisão é igual a {sobra}")
if escolha == 5.27:
    print("Exercício 5.27")
    num = int(input("Escreva o número para saber se é palíndromo ou não: "))
    original = num
    invertido = 0
    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num = num // 10
    if original == invertido:
        print(f"O número {original} é palíndromo.")
    else:
        print(f"O número {original} não é palíndromo.")