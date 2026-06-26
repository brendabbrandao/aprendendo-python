# Crie um dicionário traducao com 4 palavras em português como chave e sua tradução em inglês como valor.

# Peça ao usuário uma palavra em português. 
#
# Se ela estiver no dicionário, imprima a tradução. Se não estiver, imprima "Palavra não encontrada no dicionário."

traducao = {
    "oi":"hello",
    "tchau":"bye",
    "obrigado":"thank you"
}

palavra = input("Digite uma palavra em pt-br: ")

if palavra in traducao:
    print("A palavra em inglês é: ", traducao[palavra])
else:
    print("Palavra não encontrada no dicionário")