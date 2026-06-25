# Dado o dicionário abaixo com o estoque de uma loja, percorra-o com um for e exiba:
#— "[produto]: disponível ([qtd] unidades)" se a quantidade for maior que 0
#— "[produto]: sem estoque" se for 0

estoque = {
    "Caneta": 12, 
    "Borracha": 0, 
    "Caderno": 5, 
    "Régua": 0, 
    "Lápis": 8
}

for produto, qtde in estoque.items():
    if qtde > 0:
        print("O produto é: ", {produto}, "quantidade em estoque: ", {qtde})
    else:
        print("O produto: ", {produto}, "está sem estoque")