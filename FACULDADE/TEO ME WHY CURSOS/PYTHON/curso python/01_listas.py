# %%
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)
# %%
teo = ["Téo", "Calvo", 32, True, "Casado", 2342.98]
print(teo)
type(teo)

# %%
# nome
print(teo[0])

# idade
print(teo[2])

# renda
print(teo[5])
print(teo[-1])

# %%
idades = [28, 42, 43, 35, 39, 28, 38]
print(f"Soma das idades {sum(idades)}.")
print(f"Quantidade total de idades {len(idades)}.")
print(f"Média das idades: {sum(idades) / len(idades):.2f}.")
print(f"Maior idade: {max(idades)}.")
print(f"Menor idade: {min(idades)}.")

# %%
teo = ["Téo", 32, 
       True, "Casado",
       ["Estagiário", "ds jr", "ds.pl", "ds sr", "head"],
       [1500, 4000, 4500, 6500, 10000],
       ["Ana", "Maria", "Claudia"]]

# A lista dentro da lista conta como um elemento
print(f"Tamanho de Téo: {len(teo)}") 

print(teo[6])
exs = teo[6]
primeira_ex = teo[6][0]
print(f"Primeira Ex: {primeira_ex}")

# %%
print(teo[-1])
exs = teo[-1]
primeira_ex = teo[-1][0]
ultima_ex = teo[-1][-1]
penultima_ex = teo [-1][-2]
print(f"Primeira Ex: {primeira_ex}")
print(f"Ultima Ex: {ultima_ex} ")
print(f"Penúltima Ex: {penultima_ex}")

# %%
tamanho = len(teo)
print(teo[tamanho - 1])
exs = teo[tamanho - 1]
tamanho_exs = len(exs)
primeira_ex = teo[tamanho - 1][0]
ultima_ex = teo[tamanho - 1][tamanho_exs - 1]
print(f"Primeira Ex: {primeira_ex}")
print(f"Ultima Ex: {ultima_ex}")

# %%
print(teo[0:3]) # Ele pega o índice 0 até o 3, mas não inclui o 3

print(teo[0:4])

# %%
# Últimos dois empregos do Teo
teo[-3][-2:]

# %%
# Primeiros 4 elementos
teo[:4]

# %%
# teo[ start : stop ]

# %%
salarios = teo[-2]
print(salarios)
print(salarios[::-1])
print(salarios[::2])

# teo[ start : stop : step]

# %%
