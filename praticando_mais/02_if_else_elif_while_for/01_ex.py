#Peça a idade do usuário e classifique:
#0 a 12 → "Criança" | 13 a 17 → "Adolescente" | 18 a 59 → "Adulto" | 60 ou mais → "Idoso"

idade = input("Digite sua idade: ")

idade = int(idade)

if idade <= 12:
    print("Criança")
elif idade <= 17: 
    print("Adolescente")
elif idade <=  59:
    print("Adulto")
else:
    print("Idoso")