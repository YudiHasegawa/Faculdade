escolha = float(input("Digite o exercício desejado entre 4.6 4.8 4.9 4.10 : "))
if escolha == 4.6:
    print("Exercício 4.6")
    #Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
    #Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas
    km = float(input("Digite a distância que deseja percorrer em km: "))
    if km <= 200:
        preço = km * 0.50
        print(f"Você terá que pagar R$ {preço:.2f}.")
    else:
        preço = km * 0.45
        print(f"Você terá que pagar R$ {preço:.2f}.")
elif escolha == 4.8:
    print("Exercício 4.8")
    #Escreva um programa que leia dois números e pergunte qual operação você deseja realizar.
    #Você deve poder calcular soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada
    num_1 = float(input("Escreva o primeiro número: "))
    num_2 = float(input("Escreva o segundo número: ")) 
    operação = int(input("Digite 0 para adição, 1 para subtração, 2 para multiplicação e 3 para divisão: "))
    if operação == 0:
        resultado = num_1 + num_2
        print(f"O resultado da soma é {resultado}.")
    elif operação == 1:
        resultado = num_1 - num_2
        print(f"O resultado da subtração é {resultado}.")
    elif operação == 2:
        resultado = num_1 * num_2
        print(f"O resultado da multiplicação é {resultado}.")
    elif operação == 3:
        resultado = num_1 / num_2
        print(f"O resultado da divisão é {resultado}.")
    else:
        print("Digito inválido.")
elif escolha == 4.9:
    print("Exercício 4.9")
    #Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    #O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
    #Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
    casa = float(input("Digite o valor da casa a comprar: "))
    salário = float(input("Digite o seu salário: "))
    anos = float(input("Digite a quantidade de anos a pagar: "))
    prestação = casa / (anos * 12)
    if prestação > (salário * 0.30):
        print(f"Empréstimo não aprovado, o valor da prestação mensal é de R$ {prestação:.2f}, sendo maior que 30% do seu salário.")
    else:
        print(f"Empréstimo aprovado, o valor da prestação mental é de R$ {prestação:.2f}, sendo menor que 30% do seu salário.")
elif escolha == 4.10:
    print("Exercício 4.10")
    #Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica
    #Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios
    #Calcule o preço a pagar de acordo com a tabela a seguir
    #Tipo: Residencial | Até 500 = R$ 0,40 | Acima de 500 = R$ 0,65
    #Tipo: Comercial | Até 1000 = R$ 0,55 | Acima de 1000 = R$ 0,60
    #Tipo: Industrial | Até 5000 = R$ 0,55 | Acima de 5000 = R$ 0,60
    instalação = input("Digite de acordo com o tipo de instalação, R para residências, I para indústrias e C para comércios: ")
    if instalação == "R":
        kwh = float(input("Digite a quantidade de kWh consumida: "))
        if kwh <= 500:
            preço = 0.40
            print(f"Você terá que pagar R$ {preço:.2f} por consumo.")
        else:
            preço = 0.65
            print(f"Você terá que pagar R$ {preço:.2f} por consumo.")
    elif instalação == "I":
        kwh = float(input("Digite a quantidade de kWh consumida: "))
        if kwh <= 1000:
            preço = 0.55
            print(f"Você terá que pagar R$ {preço:.2f} por consumo.")
        else:
            preço = 0.60
            print(f"Você terá que pagar R$ {preço:.2f} por consumo.")
    elif instalação == "C":
        kwh = float(input("Digite a quantidade de kWh consumida: "))
        if kwh <= 5000:
            preço = 0.55
            print(f"Você terá que pagar R$ {preço:.2f} por consumo.")
        else:
            preço = 0.60
            print(f"Você terá que pagar R$ {preço:.2f} por consumo.")
    else:
        print("Digite uma instalação válida.")