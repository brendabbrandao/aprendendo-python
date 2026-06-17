# Dado o dicionário abaixo, percorra todos os pares e exiba cada um no formato "País: Brasil — Capital: Brasília".

capitais = {"Brasil": "Brasília", "França": "Paris", "Japão": "Tóquio"}

for pais, capital in capitais.items():   #assim acessa a chave e valor ao mesmo tempo
    print("País: ", pais, "Capital:", capital)


