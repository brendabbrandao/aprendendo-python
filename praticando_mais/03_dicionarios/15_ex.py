# Peça ao usuário que digite uma frase. 
# Separe as palavras com .split() e use um dicionário para contar quantas vezes cada palavra aparece na frase.

dicionario = {}



frase = input("Digite uma frase: ")

palavras = frase.split()  


for palavra in palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

for palavra, contador in dicionario.items():
    print("A palavra: ", palavra, "apareceu: ", contador, "vezes")


