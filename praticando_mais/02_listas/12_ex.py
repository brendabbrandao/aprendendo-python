# Crie uma lista com os números [10, -3, 0, 7, -1, 4]. 
# Percorra a lista e, para cada número, imprima se ele é positivo, negativo ou zero.

lista = [10, -3, 0, 7, -1, 4]

for item in lista:
    if item > 0:
        print("Número positivo: ", item)
    elif item  < 0:
        print("Número negativo: ", item)
    else:
        print("Zero!")
    
