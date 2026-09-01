'''
Faça o programa de uma sorveteria, onde o usuário pode escolher:
Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
Sabor do sorvete: morango, creme, chocolate
Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
'''
conta = 0
while True:
    tipo = input("""
    Uaiii, bem vindo a sorveteria!!! Bo comprar um sorvetin?
    Escolhe o tipo de sorvete manooo :)
    (1) casquinha - R$1,00
    (2) cascão - R$2,50
    (3) cestinha - R$4,00

    : """).lower()

    if tipo == "1" or tipo == "casquinha":
        tipo = "casquinha"
        conta += 1
        break
    elif tipo == "2" or tipo == "cascão":
        tipo = "cascão"
        conta += 2.50
        break
    elif tipo == "3" or tipo == "cestinha":
        tipo = "cestinha"
        conta += 4
        break
    else:
        print("Amigu, escolhe um tipo que tem ai :(")
        continue
while True:
    sabor = input("""
    Ai simmm!!!! Agora me fala o SABORRRR >:D
    (1) morango
    (2) creme
    (3) chocolate
    
    : """).lower()
    if sabor == "1" or sabor == "morango":
        sabor = "morango"
        break
    elif sabor == "2" or sabor == "creme":
        sabor = "creme"
        break
    elif sabor == "3" or sabor == "chocolate":
        sabor = "chocolate"
        break
    else:
        print("Carinha, esse sabor ai não tem, ta tirando? >:(")
        continue
while True:
    cobertura = input ("""
    Agora você sabe né? ( ͡° ͜ʖ ͡°)
    A cobertura mano!!! A cobertura!!!
    (1) caramelo - R$1,50
    (2) morango - R$1,50
    (3) chocolate - R$1,50
    (4) sem cobertura
    
    : """).lower()
    if cobertura == "1" or cobertura == "caramelo":
        cobertura = "caramelo"
        conta += 1.50
        break
    elif cobertura == "2" or cobertura == "morango":
        cobertura = "morango"
        conta += 1.50
        break
    elif cobertura == "3" or cobertura == "chocolate":
        cobertura = "chocolate"
        conta += 1.50
        break
    elif cobertura == "4" or cobertura == "sem cobertura":
        cobertura = "sem cobertura"
        break
    else:
        print("Oh bobo, escolhe uma opção válida né? (▀̿Ĺ̯▀̿ ̿)")
        continue
print(f"""
Zééé, teu sorvete ficou assim ó:
tipo: {tipo}
sabor: {sabor}
cobertura: {cobertura}

PREÇO: {conta}

Paga ai pilantra [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]""")