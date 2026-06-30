# Crie um dicionário de estoque com produtos e quantidades.
# Use um loop while para perguntar ao usuário quais produtos deseja comprar e quantas unidades. 
# Verifique se há estoque suficiente e atualize o dicionário. Encerre quando o usuário digitar sair.

estoque = {
    "agua":10,
    "farinha":20,
    "feijao":25,
    "wheyzinho":1
}

while True:
    produto= input("Digite qual produto você quer comprar | Digite sair p/ sair: ")

    if produto == "sair":
        print("Compra finalizada!")
        break
    if produto not in estoque:
        print("Produto não encontrado")
    else:
        qtde = int(input("Digite quantos produtos você deseja comprar: "))
        if qtde <= estoque[produto]:
            estoque[produto] -= qtde
            print("Produto comprado: " , produto,  "Quantidade restante: ", estoque[produto])
        else:
            print("Estoque insuficiente!")

print("Estoque final: ", estoque)
