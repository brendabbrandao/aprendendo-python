# Crie um dicionário chamado filme com as chaves "titulo" e "ano". 
# Depois, adicione a chave "genero" e altere o valor de "ano" para o ano atual. 
# Imprima o dicionário ao final.

filme = {
    "Titulo":"Toy Story",
    "Ano":"1992"
}

filme["Genero"] = "animação"

filme["Ano"] = 2026

print("Titulo: ", filme["Titulo"])
print("Ano: ", filme["Ano"])
print("Gênero: ", filme["Genero"])