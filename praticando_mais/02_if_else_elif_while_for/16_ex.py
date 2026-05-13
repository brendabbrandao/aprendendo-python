#Crie um programa que processe 3 alunos. Para cada aluno, use um for para coletar 4 notas, 
#calcule a média com um while somando as notas, e classifique com if/elif/else:

#Média ≥ 7 → "Aprovado" | Média entre 5 e 6.9 → "Recuperação" | Média < 5 → "Reprovado"


for aluno in range(1, 4):
    print("----Aluno----", aluno, "----")
    soma = 0 
    i = 1 
    while i <= 4: 
        nota =float(input("Insira a nota: "))
        soma = soma + nota
        i = i + 1 
    media = soma / 4 
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print("Média: ", media, "Situação: ", situacao)
