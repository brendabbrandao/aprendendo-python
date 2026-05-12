#Peça números ao usuário até ele digitar 0. Ao final, mostre o maior número que foi digitado.

contagem = -1 

maior = 0

while contagem != 0:
    contagem = int(input("Digite um número: | Digite 0 para parar: "))
    if contagem > maior:
        maior = contagem
print("Maior número: ", maior)