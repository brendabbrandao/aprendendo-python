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