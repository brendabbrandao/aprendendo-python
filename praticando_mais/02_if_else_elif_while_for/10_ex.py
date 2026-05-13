#Peça notas ao usuário até ele digitar -1. Ao final, mostre a média de todas as notas digitadas.

media = 0

contador = 0

nota = 0


while nota != -1:
    nota = float(input("Digite uma nota:  | Digite -1 para parar: "))
    if nota != -1:
        media = nota + contador
        contador = contador + 1
print("A média é: ", media / contador)