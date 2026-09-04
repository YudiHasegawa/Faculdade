# %%
valor = input("Entre com um valor: ") #função
print(valor) #função
print(len(valor)) #função

# %%

def nome_função (valor):
    return 1 + valor

nome_função(2)
# %%

def nome_função (valor):
    resultado = 1 + valor
    return resultado

nome_função(2)

# %%

def juros_compostos (aporte:int, taxa:float, anos:int)->float:
    """
    juros_compostos serve para calcular o retorno financeiro a partir
    de um aporte. Deve-se considerar o valor, a taxa de juros atual e
    o tempo, em anos, para o cálculo do valor a ser retornado

    aporte: um número inteiro que represente o valor em reais

    taxa: um número entre 0 e 1 que represente o valor da taxa de juros

    anos: um número inteiro >=  que represente o tempo que o investimento
    terá liquidez
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(taxa=0.13, anos=4, aporte=1000)

# %%

def juros_compostos (aporte:int, taxa:float, anos:int)->float:
    """
    juros_compostos serve para calcular o retorno financeiro a partir
    de um aporte. Deve-se considerar o valor, a taxa de juros atual e
    o tempo, em anos, para o cálculo do valor a ser retornado

    aporte: um número inteiro que represente o valor em reais

    taxa: um número entre 0 e 1 que represente o valor da taxa de juros

    anos: um número inteiro >=  que represente o tempo que o investimento
    terá liquidez
    """
    return aporte * (1 + taxa) ** anos


aporte = int(input("Digite o valor do aporte: "))
taxa = float(input("Digite o valor da taxa: "))
anos = int(input("Digite a quantidade de anos: "))

resultado = juros_compostos(aporte, taxa, anos)
print(resultado)

# %%

def ola_mundo():
    msg = "Boas Vindas! Olá pra você!"
    print(msg)

ola_mundo()
# %%

msg
# %%

def calculadora (a:int, b:int, funcao):
    '''Calculadora que calcula uma função entre dois valores.
    Podendo calcular: Adição, Subtração, Multiplicação, Divisão e Média.'''
    if funcao == "adição":
        print(f"{a} + {b} = {a + b}")
    elif funcao == "subtração":
        print(f"{a} - {b} = {a - b}")
    elif funcao == "multiplicação":
        print(f"{a} x {b} = {a * b}")
    elif funcao == "divisão":
        if b == 0:
            print("Não é possível dividir por 0")
        else:
            print(f"{a} / {b} = {a / b}")
    elif funcao == "média":
        print(f"Média: {(a + b) / 2}")
    else:
        print("Digite uma função válida")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
funcao = input("""
Escolha a função

Adição
Subtração
Multiplicação
Divisão
Média

: """).lower()
resultado = calculadora(a, b, funcao)
# %%

valores = []
x = 1

def calcular_media (valores):
    '''Calcula a média de múltiplos valores'''
    soma = 0
    contar = 0
    for n in valores:
        soma += n
        contar += 1
    media = soma / contar
    print(f"Média: {media:.2f}")
while True:
    valor = input(f"Digite o {x} valor ou ENTER para sair: ")
    if valor == "":
        break
    else:
        valores.append(float(valor))
        x += 1

resultado = calcular_media(valores)
# %%

def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto

calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional =0.001)

# %%

def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto

impostos_gerais = {
    "municipio": 0.01,
    "estadual": 0.005, 
    "nacional": 0.001
}

#calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional =0.001)
calc_imposto(100, 0.03, **impostos_gerais, internacional=0.00001)

# %%
