# A partir da lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
# crie duas listas separadas: uma com os números pares e outra com os ímpares. 
# Ao final, imprima as duas listas.

lista =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []

impares = []

for numero in lista:
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares: ", pares)
print("Númeroos ímpares: ", impares)

