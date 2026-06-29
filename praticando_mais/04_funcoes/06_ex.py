# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista de notas (4 notas). 
# Crie uma função que calcule a média e retorne a situação do aluno: 
# Aprovado (≥ 7), Recuperação (≥ 5) ou Reprovado (abaixo de 5). Itere sobre todos os alunos e imprima o relatório completo.

escola ={
    "joao":[7,10,6,5],
    "maria":[10,10,10,10],
    "alice":[10,10,10,10]
}

def calcular_situacao(notas):
    media = sum(notas)/ len(notas)

    if media >=7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
   
    return media, situacao

for aluno, notas in escola.items():
        media, situacao = calcular_situacao(notas)
        print(f"Aluno: {aluno} - Media: {media} - Situacao: {situacao}")
