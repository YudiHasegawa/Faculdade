saída = 1
while saída == 1:
    escolha = int(input("""
    Escolha o programa desejado entre 1 2 e 3, ou aperte 0 para sair:
    Programa que identifica o maior número entre 5 números (1)
    Programa que calcula o IMC e classifica em faixa (2)
    Programa que verifica que é possível realizar um triângulo com 3 valores (3)
                        
    Escolha: """))
    if escolha == 1:
        #Programa que identifica o maior número
        print("Programa que identifica o maior número")
        conjunto = []
        x = 1
        while x <= 5:
            numero = float(input(f"Digite o número {x}: "))
            if numero.is_integer():
                numero = int(numero)
            conjunto.append(numero)
            x += 1
        maior = max(conjunto)
        print(f"O maior número é o {maior}.")
    if escolha == 2:
        #Programa que calcula o IMC e classifica em faixa
        print("Programa que calcula o IMC e classifica em faixa (2)")
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros:"))
        imc = peso / (altura ** 2)
        if imc < 18.5:
            print(f"""
            Valor do IMC: {imc:.1f}
            Classificação: Abaixo do peso
            Risco de Comorbidade: Baixo
            """)
        elif imc <= 24.9:
            print(f"""
            Valor do IMC: {imc:.1f}
            Classificação: Normal
            Risco de Comorbidade: Normal
            """)
        elif imc <= 29.9:
            print(f"""
            Valor do IMC: {imc:.1f}
            Classificação: Sobrepeso
            Risco de Comorbidade: Aumentado
            """)
        elif imc <= 34.9:
            print(f"""
            Valor do IMC: {imc:.1f}
            Classificação: Obesidade (Classe I)
            Risco de Comorbidade: Moderado
            """)
        elif imc <= 39.9:
            print(f"""
            Valor do IMC: {imc:.1f}
            Classificação: Obesidade Severa (Classe II)
            Risco de Comorbidade: Grave
            """)
        elif imc >= 40:
            print(f"""
            Valor do IMC: {imc:.1f}
            Classificação: Obesidade Mórbida (Classe III)
            Risco de Comorbidade: Muito grave
            """)
    if escolha == 3:
        #Programa que verifica que é possível realizar um triângulo com 3 valores
        print("Programa que verifica que é possível realizar um triângulo com 3 valores")
        conjunto = []
        x = 1
        while x <= 3:
            numero = float(input(f"Digite o número {x}: "))
            x += 1
            conjunto.append(numero)
        conjunto.sort()
        if conjunto[0] + conjunto[1] > conjunto [2]:
            print("É possível fazer um triângulo com esses valores.")
        else:
            print("Não é possível fazer um triângulo com esses valores.")
    if escolha == 0:
        print("Fechando...")
        saída = 0
    else:
        print("\nDigite um programa válido.")