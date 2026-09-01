'''
Faça um programa que vende garrafa de água:
Se o cliente escolher água mineral natural, será cobrado R$1,50
Se o cliente escolher água mineral com gás, será cobrado R$2,50
'''
escolha = input("""
Olá!! Seja bem vindo a lojinha de aguinhas :D

Escolha a sua aguinha bem molhada
(1) Água mineral natural - R$1,50
(2) Água mineral com gás - R$2,50

: """).lower()

quantidade = int(input("Digite a quantidade desejada: "))

if escolha == ("água mineral natural") or escolha == ("1"):
    print(f"Sua conta deu: R${quantidade * 1.50}.")
elif escolha == ("água mineral com gás") or escolha == ("2"):
    print(f"Sua conta deu: R${quantidade * 2.50}.")
else:
    print("Por favor, digita uma aguinha válida. :(")