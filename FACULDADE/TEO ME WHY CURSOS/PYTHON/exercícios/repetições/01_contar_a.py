'''
Faça um programa que conte quantas vezes 
a letra “a” aparece em uma palavra
'''
palavra = input("Digite uma palavra: ")
contar = 0
for n in palavra:
    if n == "a":
        contar += 1
print(f"A palavra '{palavra}'' contém {contar} 'a'") 