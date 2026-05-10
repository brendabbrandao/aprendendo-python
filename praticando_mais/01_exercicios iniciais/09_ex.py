
alunos = 5

while alunos > 0:
    nota = input("Insira sua nota: ")
    nota = float(nota)

    if nota >= 7:
        print("Aprovado!")
    elif nota >= 5:
        print("Recuperação")
    elif nota < 5:
        print("Reprovado!")

    alunos = alunos - 1