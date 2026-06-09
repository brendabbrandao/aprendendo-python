# Faça um programa que receba dois números e diga qual deles é o maior (ou se são iguais).

n1 = input("Insira um valor:  ")
n1 = int(n1)

n2 = input("Insira um segundo valor: ")
n2 = int(n2) 

if n1 > n2:
    print("O valor N1", n1, "é maior que o N2", n2)

elif n1 < n2:
    print("O valor N1", n1, "é menor que o N2", n2)

else:
    print("Os valores são iguais")