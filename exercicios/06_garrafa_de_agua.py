#Faça um programa que vende garrafa de água:
#Se o cliente escolher agua mineral natural, é cobrado R$ 1,50 
#Se o cliente escolher agua mineral com gas, é cobrado R$ 2, 50 

#Resolução Bre: 
# tipo_de_agua =input("Digite 1 para agua mineral natural | 2 para agua mineral com gas: ")

# tipo_de_agua = int(tipo_de_agua)

# if tipo_de_agua == 1:
#     print("O valor da agua mineral natural é R$ 1,50")

# elif tipo_de_agua == 2:
#     print("O valor da agua mineral com gás é R$ 2,50")

# else:
#     print("Opção inválida")

#resolução do Teo:

texto = """ 
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gas
"""
opcao = input(texto)

if opcao == "1":
    print("Sua conta deu: R$ 1,50")

elif opcao == 2:
    print("Sua conta deu: R$ 2,50")

else:
    print("Entre com a opção correta")