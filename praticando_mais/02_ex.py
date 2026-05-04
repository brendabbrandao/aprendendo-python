#Faça um programa que receba um número inteiro e diga se ele é par ou ímpar. 

valor = input("Insira um valor numérico: ") 

valor = int(valor) 

if valor % 2 == 0:
    print("O valor: " , valor, "é um número par")

else:
    print("O valor: ", valor, "é um número ímpar") 