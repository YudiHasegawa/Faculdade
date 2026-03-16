numdisplay = 1
contador = 0
acumulador = 0
while True:
    num = int(input(f"Digite o {numdisplay} número ou aperte 0 para finalizar:"))
    if num != 0:
        acumulador += num
        numdisplay += 1
        contador += 1
    if num == 0:
        break
print(f"A média é {acumulador / contador:.2f}")
