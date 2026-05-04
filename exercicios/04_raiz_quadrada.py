#Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado 

numero_inteiro =input("Insira um número inteiro para calcular sua raiz quadrada")

numero_inteiro = int(numero_inteiro)

raiz_quadrada = numero_inteiro ** 0.5 

raiz_quadrada = round(raiz_quadrada, 4)

print("A raiz quadrada é : ", raiz_quadrada)