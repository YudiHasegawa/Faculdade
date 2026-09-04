'''
Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

Maçã: R$1,50
Banana: R$2,75
Uva: R$1,90
Pera: R$1,25
Laranja: R$0,65
Limão: R$1,25
Goiaba: R$2,15
Abacaxi: R$3,20
Jaca: R$5,80

'''
# %%
while True:
    frutas = {
        "maçã": "R$1.50",
        "banana": "R$2.75",
        "uva": "R$1.90",
        "pera": "R$1.25",
        "laranja": "R$0.65",
        "limão": "R$1.25",
        "goiaba": "R$2.15",
        "abacaxi": "R$3.20",
        "jaca": "R$5.80",
            }

    fruta = input("Entre com o noma da fruta: ").lower()

    if fruta in frutas:
        print(f"Preço: {frutas[fruta]}")
        break
    else:
        print(f"A fruta {fruta} não está no catálogo. :(")
# %%
