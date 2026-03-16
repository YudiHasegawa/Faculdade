escolha = float(input("Digite o exercício desejado entre 3.12 3.13 3.14 e 3.15 : "))
if escolha == 3.12:
    print("Exercício 3.12")
    #Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
    preço = float(input("Coloque o preço da mercadoria: "))
    porcen_desconto = float(input("Coloque a porcentagem de desconto: "))
    desconto = preço * porcen_desconto / 100
    preço_novo = preço + desconto
    print(f"O desconto será R$ {desconto:.2f}, fazendo o preço ser R$ {preço_novo:.2f}.")
if escolha == 3.13:
    print("Exercício 3.13")
    #Escreva um programa que converta uma temperatura digitada em °C em °F.
    C = float(input("Digite a temperatura em °C: "))
    F = (9 * C) / 5 + 32
    print(f"A temperatura em °F será {F:.2f}.")
if escolha == 3.14:
 print("Exercício 3.14")
 #Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantiodade de dias pelos quais o carro foi alugado.
 #Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado
 km = float(input("Coloque a quantidade de km percorridos: "))
 dias = int(input("Coloque a quantidade de dias pelos quais o carro foi alugado: "))
 valor_km = km * 0.15
 valor_dias = dias * 60
 print(f"Você terá que pagar R$ {valor_km:.2f} pela quantidade de km percorridos e R$ {valor_dias:.2f} pela quantidade de dias.")
if escolha == 3.15:
   print("Exercício 3.15")
   #Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou
   # Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias
   cigarros = int(input("Digite quantos cigarros você fuma por dia: "))
   anos = float(input("Digite quantos anos você já fumou: "))
   total_cigarros = cigarros * (anos * 365)
   minutos = total_cigarros * 10
   dias = minutos / 1440
   print(f"Você perdeu o total de {dias:.2f} dias")