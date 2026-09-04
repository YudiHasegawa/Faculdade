# %%

lista = [2, 132, "teo", ["ds", "de", "da"], True]

lista[2]

# %%

#dicionários são pares de chave/valor

dados_teo = {"nome": "Téo",
             "sobrenome": "Calvo",
             "filhos": True,
             "formação": ["estatística", "bigdata datascience"],
             "cargos": [
                 {"nome": "ds jr.", "empresa": "tapps"},
                 {"nome": "ds pl.", "empresa": "sas"},
                 {"nome": "ds sr.", "empresa": "boticario"},
                 {"nome": "ds espec.", "empresa": "via varejo"},
                 ]}

print(dados_teo)

# %%

print(dados_teo["formação"][-1])
print(dados_teo["cargos"][-1]["empresa"])

# %%

dados_teo["estado civil"] = "casado"
# %%

print(f"Chaves: {dados_teo.keys()}")
print(f"Valores: {dados_teo.values()}")
print(f"Items: {dados_teo.items()}")

# %%

for i in dados_teo:
    print(f"{i}: {dados_teo[i]}")

# %%

for items in dados_teo.items():
    print(items)

# %%

for chave, valor in dados_teo.items():
    print(f"{chave}: {valor}")
    
# %%
