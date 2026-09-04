'''
Considere a lista: [120, “Python”, 120.01, “asw”, False, [10,20] ]

Faça um programa que retorne as seguintes informações:
Elemento na posição -1 da lista
Elemento na primeira posição da lista
O último caractere do segundo elemento da lista

Elemento -1: x
Primeiro elemento: y
Último caractere do segundo elemento: z
'''

# %%

lista = [120, "Python", 120.01, "asw", False, [10,20]]

print(f"""
Elemento na última posição da lista: {lista[-1]}
Elemento na primeira posição da lista: {lista[0]}
O último caractere do segundo elemento da lista: {lista[1][-1]}
""")

# %%
