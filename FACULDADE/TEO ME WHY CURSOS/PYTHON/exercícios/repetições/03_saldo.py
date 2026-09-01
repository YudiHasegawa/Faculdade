'''
Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, 
mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, 
e exibe a soma de todos os valores digitados anteriormente.
'''
saldo_total = 0
while True:
    saldo = float(input("Digite o saldo ou 0 para sair: "))
    if saldo == 0:
        break
    else:
        saldo_total += saldo
print(f"Seu saldo total é de R${saldo_total:.2f}.")