escolha = float(input("Digite o exercício desejado entre 5.11 5.12 5.13 5.14 5.15 : "))
if escolha == 5.11:
    print("Exercício 5.11")
    #Escreva um programa que pergunte o depósito inicial, a taxa de juros de uma poupança e a quantidade de meses
    #Exiba os valores mês a mês
    #Escreva o total ganho com juros no período
    capital = float(input("Digite o deposíto inicial: "))
    taxa = float(input("Digite a taxa de juros: "))
    tempo = int(input("Digite a quantidade de meses: "))
    juros = 0
    contador = 0
    while contador < tempo:
        juros += (capital * (taxa / 100))
        contador += 1
        print(f"{contador} mês = R$ {juros:.2f}.")
    print(f"No total o ganho com juros será de R$ {juros:.2f}.")

if escolha == 5.12:
    print("Exercício 5.12")
    #Escreva um programa que pergunte o depósito inicial, a taxa de juros de uma poupança, a quantidade de meses e o valor depositado mensalmente
    #Esse valor será depositado no início de cada mês e você deve considerá-lo para o cálculo de juros do mês seguinte
    #Exiba os valores mês a mês
    #Escreva o total ganho com juros no período
    capital = float(input("Digite o deposíto inicial: "))
    deposito = float(input("Digite o depósito mensal que será adicionado a partir do segundo mês: "))
    taxa = float(input("Digite a taxa de juros: "))
    tempo = int(input("Digite a quantidade de meses: "))
    juros = 0
    contador = 1
    if contador == 1:
        juros += (capital + (capital * (taxa / 100)))
        print(f"{contador} mês = R$ {juros:.2f}.")
        contador += 1
    while contador <= tempo and contador > 1:
        juros += deposito
        juros += (juros * (taxa / 100))
        print(f"{contador} mês = R$ {juros:.2f}.")
        contador += 1
    print(f"No total o ganho com juros será de R$ {juros:.2f}.")
if escolha == 5.14:
    print("Exercício 5.14")
    #Escreva um programa que leia números inteiros do teclado. 
    #O programa deve ler os números até que o usuário digita 0 (zero)
    #No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética
    numdisplay = 1
    contador = 0
    acumulador = 0
    while True:
        num = int(input(f"Digite o {numdisplay} número ou aperte 0 para finalizar:"))
        if num != 0:
            acumulador += num
            numdisplay += 1
            contador += 1
        if num == 0:
            break
    print(f"""
    A quantidade de números digitados é: {contador}. 
    A soma dos números é {acumulador}.
    A média é {acumulador / contador:.2f}.
    """)
if escolha == 5.15:
    print("Exercício 5.15")
    #Escreva um programa para controlar uma pequena máquina registradora.
    #Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
    #Seu programa deve exibir o total das compras depois que o usuário digitar 0
    #Qualquer outro código deve gerar a mensagem de erro "Código inválido"
    #Utilize a tabela de códigos a seguir para obter o preço de cada produto: código 1 - 0,50 / código 2 - 1,00 / código 3 - 4,00 / código 5 - 7,00 / código 9 - 8,00
    print("""
    Código 1 - Preço: 0,50
    Código 2 - Preço 1,00
    Código 3 - Preço: 4,00
    Código 5 - Preço: 7,00
    Código 9 - Preço: 8,00
    """)
    quantidade1 = 0
    quantidade2 = 0
    quantidade3 = 0
    quantidade5 = 0
    quantidade9 = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total5 = 0
    total9 = 0
    while True:
        código = int(input("Digite o código do produto ou digite 0 para prosseguir: "))
        if código == 0:
            break
        if código == 1:
            quantidade1 = int(input("Digite a quantidade de produtos: "))
            total1 = quantidade1 * 0.5
        if código == 2:
            quantidade2 = int(input("Digite a quantidade de produtos: "))
            total2 = quantidade2 * 1
        if código == 3:
            quantidade3 = int(input("Digite a quantidade de produtos: "))
            total3 = quantidade3 * 4
        if código == 5:
            quantidade5 = int(input("Digite a quantidade de produtos: "))
            total5 = quantidade5 * 7
        if código == 9:
            quantidade9 = int(input("Digite a quantidade de produtos: "))
            total9 = quantidade9 * 8
        elif código != 1 and código != 2 and código != 3 and código != 5 and código != 9:
            print("Código inválido")
    print()
    if quantidade1 > 0:
        print(f"Código 1 ({quantidade1}): R$ {total1:.2f}.")
    if quantidade2 > 0:
        print(f"Código 2 ({quantidade2}): R$ {total2:.2f}.")
    if quantidade3 > 0:
        print(f"Código 3 ({quantidade3}): R$ {total3:.2f}.")
    if quantidade5 > 0:
        print(f"Código 5 ({quantidade5}): R$ {total5:.2f}.")
    if quantidade9 > 0:
        print(f"Código 9 ({quantidade9}): R$ {total9:.2f}.")
    
print(f"\nO total será: R$ {total1 + total2 + total3 + total5 + total9:.2f}.")