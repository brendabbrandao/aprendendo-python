# Fique pedindo números ao usuário e somando tudo. Quando ele digitar 0, pare e exiba o total acumulado.

soma = 0
contador = 1

while contador != 0:
    numero = int(input("Digite um número:  | 0 para parar"))
    soma = soma + numero 
    contador = numero 
print("O total acumulado é de: ", soma)