# Você tem uma lista de produtos com preços: [("café", 8.50), ("arroz", 22.90), ("chocolate", 12.00), ("água", 3.50), ("vinho", 85.00)].
# Percorra a lista e aplique as seguintes regras de desconto no preço final: 
# produtos com preço acima de R$ 50 → 20% de desconto; 
# entre R$ 10 e R$ 50 → 10% de desconto; 
# abaixo de R$ 10 → sem desconto. 
# Imprima o nome, preço original e preço final de cada produto. 
# Ao final, some o total da compra.

mercadinho_maquinas_termicas = [("café", 8.50), ("arroz", 22.90), ("chocolate", 12.00), ("água", 3.50), ("vinho", 85.00)]

desconto = 0
total = 0


for nome, preco in mercadinho_maquinas_termicas:
    if preco > 50:
        preco_final = preco - (preco * 0.20)
        print("O produto é: ", nome, "o preço é: ", preco, "com desconto fica: ", preco_final)
    elif preco >= 10 and preco < 50:
        preco_final = preco - (preco * 0.10)
        print("O produto é: ", nome, "o preço é: ", preco, "com desconto fica: ", preco_final)
    else:
        preco_final = preco
        print("O produto é: ", nome, "o preço é: ", preco, "nessa faixa não há desconto")

    total = preco_final + total     


print("O valor da compra é: ", total)
