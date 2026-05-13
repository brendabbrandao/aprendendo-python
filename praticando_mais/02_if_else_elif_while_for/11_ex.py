#Peça um número N ao usuário e use for para somar todos os números de 1 até N. Mostre o resultado.

numero = int(input("Digte um número: "))
soma = 0 

for cada_numero in range(1, numero + 1): 
    soma = soma + cada_numero
print("A soma é: ", soma)
