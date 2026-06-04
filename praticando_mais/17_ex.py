# Peça um número n ao usuário. Exiba todos os números pares de 0 até n, um por linha.

n = int(input("Digite um número: "))

for i in range (0, n):
    if i % 2 == 0:
        print(i)