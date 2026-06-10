#Peça ao usuário 5 nomes, um por vez, e vá adicionando cada um numa lista. 
# No final, exiba a lista completa e quantos nomes foram digitados.

nomes = []
contador = 0

while contador < 5:
    nome = input("Digite um nome: ")
    nomes.append(nome)
    contador = contador + 1
print("A lista completa de nomes é: ", nomes, "com o tamanho: ", len(nomes))

