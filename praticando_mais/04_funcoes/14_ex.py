# Crie uma função chamada separar_pares_impares(numeros) que recebe uma lista de números inteiros
#  e retorna uma tupla contendo duas listas: (lista_pares, lista_impares). 
# Use um for para percorrer a lista original e classificar cada número. 
# Exemplo: separar_pares_impares([1, 2, 3, 4, 5, 6]) deve retornar ([2, 4, 6], [1, 3, 5]).

def separar_pares_impares(lista_numeros):
    lista_pares = []
    lista_impares= []
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
    return lista_pares, lista_impares

lista_numeros = [1, 2, 3, 4, 5, 6]

resultado = separar_pares_impares(lista_numeros)

print(resultado)

