#Peça um número N e imprima uma escada de estrelas com N degraus usando for.

n = int(input("Digite um número N: "))

escada = "*"

for indice in range (1, n+1):
  print("*" * indice)

