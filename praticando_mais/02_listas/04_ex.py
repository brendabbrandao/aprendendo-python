# Crie uma lista com 6 números. 
# Sem usar max() ou min(), percorra a lista e descubra qual é o maior e qual é o menor número.

numeros = [6, 7, 12, 33, 45, 28]

maior = numeros[0]
menor = numeros[0]

for i in numeros:
    if i > maior:
        maior = i 
    if i < menor:
        menor = i
print("O maior número é:" , maior)
print("O menor número é: ", menor)
    