#Solicite ao usuário uma fruta e imprima o preço correspondente

fruta = input("Entre com o nome da fruta: ")

frutas ={
        "Pera": "R$ 1,25",
        "Maça": "R$ 2,25",
        "Goiaba": "R$ 3,20",
        "Laranja": "R$ 5,80"
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor válido!")