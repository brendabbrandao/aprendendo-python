#Peça números ao usuário repetidamente. 
#Para cada número, diga se é positivo ou negativo. 
# Quando ele digitar 0, pare e mostre quantos positivos e quantos negativos foram digitados.


positivo = 0 

negativo = 0 

numero = -1 

while numero != 0:
    numero = int(input("Digite um número: | Digite 0 para parar"))
    if numero > 0:
        print("Número positivo!")
        positivo = positivo + 1
    elif numero < 0: 
        print("Número negativo!")
        negativo = negativo + 1
print("Poisitivos: ", positivo, "Negativos: ", negativo)