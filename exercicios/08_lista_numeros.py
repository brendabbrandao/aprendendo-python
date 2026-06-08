#Escreva um programa que receba uma lista de números
#do usuário e conte quantas vezes um número
#específico aparece na lista.
#Solicite ao usuário um número e exiba a contagem 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1]

numero = int(input("Digite um número: "))

contador = 0

for i in lista:
    if i == numero:
        contador += 1
print("Quantidade de vezes que o", numero,  "aparece:", contador)