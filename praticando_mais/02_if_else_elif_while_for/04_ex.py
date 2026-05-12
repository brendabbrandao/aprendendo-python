#Peça um número inteiro. Se for 0, diga "zero". Se for par, diga "par". Se for ímpar, diga "ímpar".

numero = int(input("Digte um número inteiro: "))
if numero == 0:
    print("Zero")
elif numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")