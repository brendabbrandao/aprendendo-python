#Escreva um programa que solicite ao usuário frases. Para parar de solictar
#frases, ele pode apenas apertar o "enter".
#Seu programa deve apresentar cada frase e quantas vezes ela foi repetida,
# ordenando valores 

dados = {}

while True:
    frase = input("Digite uma frase: ") 
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1   # o que estiver na frase vira chave no dict
    else:
        dados[frase] += 1

for i in dados:
    print(i, "->", dados[i])


