# Crie um programa de carrinho de compras. 
# Use um while para permitir que o usuário adicione produtos e preços. 
# Quando digitar "finalizar", o programa deve parar e exibir:

# — todos os produtos adicionados (com seus preços)
# — o total gasto
# — uma mensagem "Frete grátis!" se o total for maior que R$ 150, ou "Frete: R$ 15.00" caso contrário

#Chave - produto | Valor - preço

carrinho = {}
total = 0 

while True:
    produto = input("Digite um produto ou finalizar: ")
    if produto == "finalizar":
          break

    preco = float(input("Digite o preço do produto: "))

    carrinho[produto] = preco
    total = total + preco 

for produto, preco in carrinho.items():
     print("Produto:", produto)
     print("Preço:" , preco)
     
print("O preço total é:", total)

if total > 150:
     print("Frete grátis")
else:
     print("Frete R$ 15")



        



