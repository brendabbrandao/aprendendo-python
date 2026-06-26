# Você tem o dicionário:

# Peça ao usuário um produto. Use if com in para verificar se o produto está no estoque.  

# Se estiver, imprima a quantidade. Se não estiver, imprima "Produto não encontrado."

estoque = {
    "arroz": 50, 
    "feijão": 30, 
    "macarrão": 0
    }

produto = input("Digite um produto: ")

if produto in estoque:
    print("Quantidade: ", {estoque[produto]})
else:
    print("Produto não encontrado")