escolha = float(input("Digite o exercício desejado entre 4.2 4.3 4.4 e 4.5: "))
if escolha == 4.2:
 print("Exercício 4.2")
 #Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado
 #Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h
 velocidade = float(input("Digite a velocidade do carro em km: "))
 if velocidade > 80:
  multa = (velocidade - 80) * 5
  print(f"Você foi multado e terá que pagar R$ {multa:.2f}.")
 else:
  print("Você não foi multado.")
elif escolha == 4.3:
 print("Exercício 4.3")
 #Escreva um programa que leia três números e que imprima o maior e o menor
 num_1 = float(input("Digite o primeiro número: "))
 num_2 = float(input("Digite o segundo número: "))
 num_3 = float(input("Digite o terceiro número: "))
 if num_1 > num_2 and num_1 > num_3:
  print(f"O número {num_1} é o maior.")
 if num_2 > num_1 and num_2 > num_3:
  print(f"O número {num_2} é o maior.")
 if num_3 > num_1 and num_3 > num_2:
  print(f"O número {num_3} é o maior.")
 if num_1 < num_2 and num_1 < num_3:
  print(f"O número {num_1} é o menor.")
 if num_2 < num_1 and num_2 < num_3:
  print(f"O número {num_2} é o menor.")
 if num_3 < num_1 and num_3 < num_2:
  print(f"O número {num_3} é o menor.")
elif escolha == 4.4:
 print("Exercício 4.4")
 #Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento
 #Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
 #Para os inferiores ou iguais, de 15%
 salário = float(input("Digite o seu salário: "))
 if salário > 1250.00:
  aumento = salário + (salário * 0.10)
  print(f"Seu salário de R$ {salário:.2f} aumentará para R$ {aumento:.2f}")
 else:
  aumento = salário + (salário * 0.15)
  print(f"Seu salário de R$ {salário:.2f} aumentará para R$ {aumento:.2f}")
else:
 print("Inválido, digite um exercício válido.")