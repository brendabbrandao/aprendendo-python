#Crie um dicionário com 4 itens de um cardápio e seus preços. 
# Peça ao usuário um item e exiba o preço. Se o item não existir, exiba "Item não encontrado."

cardapio = {
    "Refri":5,
    "Batatinha":10,
    "Burgo":15,
    "Pudim":12.50
}

pedido = input("Digite um item: ")
if pedido in cardapio:
    print("O item é:", pedido, "o valor é: ", cardapio[pedido])  
else:
    print("Item não encontrado!")