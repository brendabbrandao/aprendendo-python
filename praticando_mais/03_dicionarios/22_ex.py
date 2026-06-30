# Peça ao usuário uma palavra. 
# Percorra cada letra da palavra e crie um dicionário
#  onde cada chave é uma letra e o valor é a quantidade de vezes que ela aparece.

contagem = {}


palavra = input("Digite uma palavra: ")

for letra in palavra:
    if letra in contagem: 
        contagem[letra] += 1 
    else:
        contagem[letra] = 1 

print(contagem )