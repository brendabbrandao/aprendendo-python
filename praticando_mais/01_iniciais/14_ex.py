# Defina uma senha fixa no código (ex: "python"). 
# Fique pedindo ao usuário que digite a senha até acertar. Quando acertar, exiba "Acesso liberado!".

senha = "supersenha"

tentativa = input("Digite a senha: ")

while tentativa != senha:
    print("Senha incorreta. Digite novamente")
    tentativa = input("Digite a senha: ")

print("Acesso liberado")