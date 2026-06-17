# Crie uma lista com 3 dicionários, cada um representando um aluno com "nome" e "nota". 
# Percorra a lista com um for e exiba o nome e a nota de cada aluno.

lista =[
    {"Nome":"Joao", "Nota": 5}, 
    {"Nome":"Maria","Nota": 6}, 
    {"Nome":"Marijoao","Nota":7}  
]

for i in lista:
    print(i["Nome"], i["Nota"])