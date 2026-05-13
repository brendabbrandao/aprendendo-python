#Peça um número N e calcule o seu fatorial (N! = 1 × 2 × 3 × ... × N) usando for.

n = int(input("Digite um número N: "))

fatorial = 1

for indice in range(1, n+1):
    fatorial = fatorial * indice
print("O número fatorial é: ", fatorial)

