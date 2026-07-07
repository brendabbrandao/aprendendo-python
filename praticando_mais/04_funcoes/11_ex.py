# Crie uma função soma_pares(numeros) que recebe uma lista de números inteiros 
# e retorna a soma de todos os números pares, usando um for. 
# Exemplo: soma_pares([1,2,3,4,5,6]) deve retornar 12.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def soma_pares(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma = soma + numero
    return soma

resultado = soma_pares(lista_numeros)

print(resultado)