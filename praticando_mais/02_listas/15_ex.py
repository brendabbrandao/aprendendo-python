# Você tem uma lista de notas: [9.5, 4.0, 7.2, 5.9, 8.1, 3.3, 6.0]. 
# Para cada nota, classifique e imprima: Aprovado (≥ 7), Recuperação (entre 5 e 6.9) ou Reprovado (< 5).

notas = [9.5, 4.0, 7.2, 5.9, 8.1, 3.3, 6.0]

for nota in notas:
    if nota > 7:
        print("Aprovado: ", nota)
    elif nota < 6.9:
        print("Recuperação", nota)
    else:
        print("Reprovado", nota)