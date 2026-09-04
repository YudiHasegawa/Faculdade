'''
Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

	O número x é impar
ou
	O número x é par
'''
# %%
def par_impar (numero:int):
    '''Verifica se o número é par ou ímpar.'''
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número: "))
resultado = par_impar(numero)

print(f"O número {numero} é {resultado}!!!")
# %%
 