# Peça um número ao usuário. Se for maior que zero, exiba "Positivo". Se for menor, exiba "Negativo". Se for igual a zero, exiba "Zero".

numero = float(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
elif numero == 0:
    print("Zero")
else:
    print("Número negativo")