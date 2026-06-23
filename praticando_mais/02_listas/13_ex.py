# Dada a lista ["banana", "abacaxi", "uva", "abacate", "laranja", "amora"], 
# percorra a lista e imprima apenas as frutas que começam com a letra "a".

lista_frutas = ["banana", "abacaxi", "uva", "abacate", "laranja", "amora"]

for fruta in lista_frutas:
    if fruta.startswith("a"):
        print("A fruta começa com A: ", fruta)
    else:
        print("A fruta não começa com A: ", fruta)