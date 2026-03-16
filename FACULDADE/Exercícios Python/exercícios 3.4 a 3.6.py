print("Exercício 3.4")
#Escreva uma expressão para determinar s e uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
salário = float(input("Digite o seu salário: "))
if salário > 1200:
    print("Você deve pagar imposto, se ferrou kk.")
else: 
    print("Você não precisa pagar imposto, pobre lascado.")
print("Exercício 3.5")
#Calcule o resultado da expressão A > B and C or D, utilizando os valores a seguir.
print("primeira situação")
A = 1
B = 2
C = True
D = False
resultado = A > B and C or D
print(resultado)
print("segunda situação")
A = 10
B = 3
C = False
D = False
resultado = A > B and C or D
print(resultado)
print("terceira situação")
A = 5
B = 1
C = True
D = True
resultado = A > B and C or D
print(resultado)
print("Exercício 3.6")
#Escreva uma expressão que será utilizada para decidir se um aluno foi aprovado ou não. Para ser aprovado, o aluno todas as médias do aluno devem ser maiores que 7.
#Considere que o aluno cursa apenas 3 matérias.
nota1 = float(input("Digite a média da primeira matéria: "))
nota2 = float(input("Digite a média da segunda matéria: "))
nota3 = float(input("Digite a média da terceira matéria: "))
if nota1 > 7 and nota2 > 7 and nota3 > 7:
    print("Você foi aprovado, fez o mínimo.")
else:
    print("Você foi reprovado, bixin burro kk.")