#Peça ao usuário um número e exiba a tabuada completa dele, do 1 ao 10.

numero = input("Insira um número: ")

numero = int(numero)

for i in range(1, 11):
    print (numero, "X", i, "=", numero * i)