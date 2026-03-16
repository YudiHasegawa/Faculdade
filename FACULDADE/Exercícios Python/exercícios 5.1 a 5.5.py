escolha = float(input("Digite o exercício desejado entre 5.1 5.2 5.3 5.4 5.5 : "))
if escolha == 5.1:
    print("Exercício 5.1")
    #Faça um programa para exibir os números de 1 a 100
    x = 1
    while x <= 100:
        print(x)
        x = x + 1 
        #O x no final vira 101 por mais que ele mostre até o 100
        #Para realmente ser 100 no final e mostrar, acho que teria que colocar if x = 100: print(x)
elif escolha == 5.2:
    print("Exercício 5.2")
    #Faça um programa para exibir os números de 50 a 100
    x = 50
    while x <= 100:
        print (x)
        x = x + 1 
        #O x no final vira 101 por mais que ele mostre até o 100
        #Para realmente ser 100 no final e mostrar, acho que teria que colocar if x = 100: print(x)
elif escolha == 5.3:
    print("Exercício 5.3")
    #Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
    x = 10
    while x >= 0:
        print(x)
        x = x - 1
    if x < 0:
        print("Fogo!!!")
elif escolha == 5.4:
    print("Exercício 5.4")
    #Faça um programa que imprima de 1 até o último digitado pelo usuário, mas apenas os números ímpares
    fim = int(input("Digite quantos números deseja contar: "))
    x = 1
    while x <= fim:
        if x % 2 >= 1:
            print(x)
        x = x + 1
elif escolha == 5.5:
    print("Exercício 5.5")
    #Fala um programa para escrever os 10 primeiros múltiplos de 3
    x = 3
    while x <= 30:
        print(x)
        x = x + 3