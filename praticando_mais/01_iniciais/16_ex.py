# Peça ao usuário um número n. Some todos os números de 1 até n e exiba o resultado no final.

n = int(input("Digite um número: "))
soma = 0 

for i in range(1, n + 1):
    soma = soma + i

print("A soma total é: ", soma)