#Faça um programa que exiba o dobro de um número inserido pelo usuário.
try:
    numero = int(input("Digite um número inteiro para calcular o dobro: "))
    dobro = numero * 2
    print(f"{numero} x 2 = {dobro}")
except ValueError:
    print("Digite um número inteiro, por favor. :(")