# %%
idades = [17, 32, 56, 87]
print(idades)

# %%
idades.append(32)
print(idades)

#O append sempre adiciona na última posição

# %%
idades = []
while True:
    idade = int(input("Entre com a idade ou 0 para sair: "))
    if idade == 0:
        break
    else:
        idades.append(idade)
total = len(idades)  
soma = sum(idades)   
media = soma / total 
maior = max(idades)  
menor = min(idades)  

print(idades)
print(f"""
Total de idades: {total}
Média das idades: {media:.2f}
Maior idade: {maior}
Menor idade: {menor}
""")

# %%
