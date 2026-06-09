#Peça a idade do usuário. Se tiver 18 anos ou mais, exiba "Pode entrar!". 
# Se tiver entre 16 e 17 anos, exiba "Pode entrar somente acompanhado.". 
# Se for menor de 16, exiba "Não pode entrar."

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode entrar!")
elif idade >= 16:
    print("Pode entrar acompanhado")
else:
    print("Não pode entrar!")