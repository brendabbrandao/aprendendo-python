#Peça ao usuário 3 nomes e 3 idades, um por vez. 
# Armazene tudo num dicionário onde a chave é o nome e o valor é a idade. Exiba o dicionário no final.

contador = 0 
pessoas = {}

while contador < 3: 
    nome =input("Digite um nome: ")
    idade = input("Digite uma idade: ")
    contador = contador + 1 
    pessoas[nome] = idade

print(pessoas)
