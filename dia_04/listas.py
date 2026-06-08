#Listas: maneira de adicionar vários elemtentos

#Uma maneira de definir listas 
idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)

brenda =['Brenda', 'Brandao', False, '28', 'Noiva', 1]
print(brenda)

#Desocbrir o tipo de uma váriavel: 
type(brenda)

# Acessar os elementos de uma lista 
#O indice começa no 0
#Quero acessar a idade
print(brenda[3])

#Primeiro elemento (indice) da lista
print(brenda[0])


#Propriedades - respeite as regras

idades = [28, 42, 43, 35, 39, 28, 38]

#Qual a soma de todos elementos dessa lista? 
print("Soma das idades: ", sum(idades))

#Média das idades
print("A média das idades: ", sum(idades)/ len(idades))

#Descobrir o tamanho da lista
print("qtde idades: ", len(idades))    #len diz o tamanho da lista 

#Descobrir a menor idade 
print("A menor idade é: ", min(idades))

#Descobrir a maior idade
print("A maior idade é: ", max(idades))


#Como descobrir quem é a primeira da lista de garotas
brenda =['Brenda Brandao', False, '28', 'Noiva', ['Estag', 'Jr', 'Pl', 'Sr'], [1, 2, 3, 4] , ['Ana', 'Maria', 'Claudia'] ]
brenda[4][0]  #é a mesma coisa que abaixo | acessando elementos da lista  | agora com mais mudou a posição

garotas = brenda[4]
primeira_girl = garotas[0]
print(primeira_girl)

#como acessar a primeira sem chumbar um número?
tamanho = len(brenda)
pos = tamanho - 1
print(brenda[pos])

#como acessar o ultimo sem chumbar o numero?
brenda[-1]   #-1 é o ultimo elemento da minha lista 

#como acessar o penultimo elemento?
brenda[-2]