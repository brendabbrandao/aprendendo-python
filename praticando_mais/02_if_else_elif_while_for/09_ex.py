#Comece com o número 1. 
#Fique dobrando ele (multiplicando por 2) enquanto for menor que 1000. Mostre cada valor e, ao final, quantas vezes dobrou..

inicio = 1 
vezes = 0 

while inicio < 1000:
    print(inicio)
    inicio = inicio * 2 
    vezes = vezes + 1 
print("Dobrou esse tanto de vezes: ", vezes)