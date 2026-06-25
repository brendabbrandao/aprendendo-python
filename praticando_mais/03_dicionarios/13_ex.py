# Crie um dicionário produtos com 3 itens e seus preços (ex: "arroz": 5.50). 
# Use um laço for com .items() para imprimir cada produto e seu preço no formato: arroz custa R$ 5.50.

produtos = {
    "Batata frita":9.5,
    "Burgo":10,
    "Pizza":25
}

for produto, preco in produtos.items():
    print("O produto é: ", {produto}, "o preço é: ", {preco})