'''
Escreva um programa que solicite ao usuário frases. 
Para parar de solicitar frases, ele pode apenas apertar o “enter”.
Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.
'''


frases = []
dict_frases = {}
while True:
    frase = input("\nDigite uma frase ou pressione ENTER para sair: ")
    if frase == "":
        break
    frases.append(frase)

for n in frases:
    if n in dict_frases:
        dict_frases[n] += 1
    else:
        dict_frases[n] = 1

items = list(dict_frases.items())
items.sort(key=lambda x: x[-1], reverse=True)

for frase, quantidade in items:
    print(f"\n{frase} apareceu {quantidade} vez(es).")