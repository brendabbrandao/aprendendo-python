# Dada a lista de notas abaixo, crie uma nova lista só com as notas maiores ou iguais a 7. Exiba as duas listas ao final.

notas = [5, 8, 3, 7, 9, 4, 6, 10]

aprovados = []

for nota in notas:
    if nota >= 7:
        aprovados.append(nota)


print("A lista com todas as notas é: ", notas)
print("A lista de aprovados é: ", aprovados)

