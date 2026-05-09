#Faça um programa que receba uma quantidade indefinida de valores correspondentes a "saldo em conta",
#mas, quando o usuário apertar "enter", sem digitar valor algum, o programa para de receber valores,
#e exibe a soma de todos os valores digitados anteriormente 

#maneira de sair do laço while de maneira forçada, quando ele é acionado ele vai sair do primeiro laço que ele encontra

#só sai do laço while se a condição for falsa ou se aparecer um break 

saldo_total = 0 

while True:
    saldo = input("Entre com o saldo: " )
    if saldo == "":
        break      
    saldo_total  += float(saldo)

print(saldo_total)
