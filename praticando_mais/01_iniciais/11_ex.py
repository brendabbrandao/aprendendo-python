# Peça uma nota de 0 a 10. 
# Se for maior ou igual a 7, exiba "Aprovado". 
# Se estiver entre 5 e 6.9, exiba "Recuperação". Se for menor que 5, exiba "Reprovado".

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado!")
elif nota <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")