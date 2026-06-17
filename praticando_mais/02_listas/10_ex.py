#Dada a lista de notas abaixo, calcule e exiba a média da turma.

notas = [7, 9, 5, 8, 6, 10, 4, 7]

media = 0

for nota in notas:
    media = media + nota

total = media / len(notas)


print("A média é: ", total)

