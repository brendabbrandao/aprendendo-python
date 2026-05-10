#Defina uma senha no código (ex: 1234). 
# #Fique pedindo a senha ao usuário até ele digitar a correta. 
# A cada tentativa errada, mostre "Senha incorreta, tente de novo." Quando acertar, mostre "Acesso liberado!"


senha = "1234"

tentativa = ""

while tentativa != senha:
    tentativa = input ("Insira a senha: ")
    if tentativa != senha:
        print("Senha incorreta, tente novamente")

print("Acesso liberado!")