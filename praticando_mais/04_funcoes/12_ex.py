# Crie uma função estatisticas(numeros) que recebe uma lista de números
#  e retorna uma tupla (menor, maior, media). Chame a função e desempacote o resultado em três variáveis.


def estatisticas(numeros):
    menor = min(numeros)
    maior = max(numeros)
    media = sum(numeros) / len(numeros)
    return menor, maior, media 

lista = [16, 27, 28, 29, 15]

menor, maior, media = estatisticas(lista)

print("Menor número: ", {menor})
print("Maior número: ", {maior})
print("Média: ", {media})