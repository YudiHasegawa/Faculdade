#Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.
contar = 1
soma = 0
while contar <= 4:
    altura = float(input(f"Digite a {contar} altura em metros: "))
    soma += altura
    contar += 1
print(f"A soma total das alturas é {soma:.2f} metros")