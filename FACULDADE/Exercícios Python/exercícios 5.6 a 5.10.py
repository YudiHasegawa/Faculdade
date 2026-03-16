escolha = float(input("Digite o exercício desejado entre 5.6 5.7 5.8 5.9 5.10 : "))
if escolha == 5.6:
    print("Exercício 5.6")
    #Faça um programa para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4,...
    num = int(input("Digite um número inteiro para a sua tabuada: "))
    x = 1
    while x <= 10:
        resultado = num * x
        print (f"{num} x {x} = {resultado}")
        x = x + 1
elif escolha == 5.7:
    print("Exercício 5.7")
    #Faça um programa para exibir os resultados no mesmo formato de uma tabuada, porém o usuário pode digitar o início e o fim da tabuada, em vez de começar com 1 e 10.
    inicio = int(input("Digite o começo da tabuada: "))
    fim = int(input("Digite o fim da tabuada: "))
    num = int(input("Digite o número para a sua tabuada: "))
    while inicio <= fim:
        resultado = num * inicio
        print (f"{num} x {inicio} = {resultado}")
        inicio = inicio + 1
elif escolha == 5.8:
    print("Exercício 5.8")
    #Faça um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo
    #Utilize apenas os operadores de soma e subtração para calcular o resultado.
    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))
    resultado = num_1
    contador = 1
    while contador < num_2:
        resultado = resultado + num_1
        contador = contador + 1
    else:
        print(f"O resultado da multiplicação é igual a {resultado}")
elif escolha == 5.9:
    print("Exercício 5.9")
    #Faça um programa que leia dois números. Imprima o resultado da divisão do primeiro pelo segundo
    #Utilize apenas os operadores de soma e subtração para calcular o resultado.
    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))
    quociente = num_1
    contador = 0
    while quociente > 0:
        quociente -= num_2
        contador = contador + 1
    else:
        print(f"O resultado da divisão é igual a {contador}")
elif escolha == 5.10:
    print("Exercício 5.10")
    #Faça um programa com 4 questões e 4 alternativas em cada, coloque uma das alternativas como correta e no final indique quantas questões o usuário acertou
    #Faça com que o programa aceita respostas com letras maiúsculas e minúsculas em todas as questões
    acertos = 0
    questão = 4
    acumulador = 1
    while acumulador < 4:
        if acumulador == 1:
            print("""
            Exercício 1 - Quanto é 2 + 2?
    
            a) 3
            b) 0
            c) 4
            d) 16
            """)

        resposta = input("Digite a alternativa correta: ")
        if acumulador == 1 and (resposta == "c" or resposta == "C"):
            acertos += 1
        acumulador += 1
        if acumulador == 2:
            print("""
            Exercício 2 - Quanto é 3 - 2?
    
         a) 5
         b) 1
         c) 2
         d) 6
         """)

        resposta = input("Digite a alternativa correta: ")
        if acumulador == 2 and (resposta == "b" or resposta == "B"):
            acertos += 1
        acumulador += 1
        if acumulador == 3:
            print ("""
            Exercício 3 - Quanto é 7 vezes 2?
        
            a) 14
            b) 9
            c) 5
            d) 16
            """)

            resposta = input("Digite a alternativa correta: ")
        if acumulador == 3 and (resposta == "a" or "A"):
            acertos += 1
        acumulador += 1
        if acumulador == 4:
            print ("""
            Exercício 4 - Quanto é 12 dividido por 6
        
            a) 2
            b) 4
            c) 8
            d) 6
            """)

            resposta == input("Digite a alternativa correta: ")
        if acumulador == 4 and (resposta == "a" or resposta == "A"):
            acertos += 1
        acumulador += 1
    else:
        nota = acertos * (10 / questão)
        print(f"Você acertou {acertos} de {questão} questões, sua nota é {nota}.")

