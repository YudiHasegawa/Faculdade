"""
Tarefa: Implementar um programa que armazene medições em uma lista e gere um relatório aleatório.
Requisitos:
Ler N valores (float) e armazenar em uma lista
Calcular média, maior, menor
Criar uma lista com apenas valores acima da média
"""
lista = []
lista_especial = []
x = 1
maior = 0
soma = 0
while True:
    try:
        número = float(input(f"\nDigite o {x} número ou 0 para sair: "))
        if número == 0:
            break
        lista.append(número)
        x += 1
    except ValueError:
        print("\nValor inválido. Tente novamente.")
lista.sort
for n in lista:
    soma = soma + n
    média = soma / len(lista)
    if n > maior:
        maior = n
for n in lista:
    if n > média:
        lista_especial.append(n)
menor = lista[0]
print(f"""
A média dos valores é: {média:.2f}
O maior valor é: {maior}
O menor valor é: {menor}
Lista com valores acima da média: {lista_especial}
""")