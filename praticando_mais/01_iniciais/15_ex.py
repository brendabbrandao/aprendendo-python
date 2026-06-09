#Peça um número ao usuário e exiba a tabuada completa dele, de 1 a 10.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    numero = numero * i
    print(numero)