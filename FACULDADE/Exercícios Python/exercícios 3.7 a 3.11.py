escolha = float(input("Digite o exercício desejado entre 3.7 3.8 3.9 3.10 e 3.11 :"))
if escolha == 3.7:
 print("Exercício 3.7")
 #Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela
 num_1 = int(input("Digite o primeiro número inteiro: "))
 num_2 = int(input("Digite o segundo número inteiro: "))
 resultado = num_1 + num_2
 print(f"A soma dos dois números inteiros é igual a {resultado}.")
if escolha == 3.8:
 print("Exercício 3.8")
 #Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
 metros = float(input("Digite o valor em metros: "))
 conversão = metros * 1000
 print(f"{metros} metros em milímetros equivale a {conversão:.2f}.")
if escolha == 3.9:
 print("Exercício 3.9")
 #Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos
 dias = int(input("Digite o número de dias: "))
 horas = int(input("Digite o número de horas: "))
 minutos = int(input("Digite o número de minutos: "))
 segundos = int(input("Digite o número de segundos: "))
 dias_conver = dias * 86_400
 horas_conver = horas * 3600
 minutos_conver = minutos * 60
 resultado = dias_conver + horas_conver + minutos_conver + segundos
 print(f"O total de segundos é: {resultado}.")
if escolha == 3.10:
 print("Exercício 3.10")
 #Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
 salário = float(input("Coloque o seu salário: "))
 porcen_aumento = float(input("Coloque a porcentagem do aumento: "))
 aumento = salário * porcen_aumento / 100
 salário_novo = salário + aumento
 print(f"O seu aumento será R$ {aumento:.2f} e o seu salário será {salário_novo:.2f}.")
if escolha == 3.11:
 print("Exercício 3.11")
 #Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para viagem
 distância = float(input("Digite a distância em km a percorrer: "))
 velocidade = float(input("Digite a velocidade média em km/h esperada para a viagem: "))
 tempo = distância / velocidade
 print(f"O tempo da viagem será de {tempo:.2f} horas.")