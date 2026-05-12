#Peça o valor de uma compra. Aplique o desconto:
#abaixo de R$50 → sem desconto | R$50 a R$99 → 10% | R$100 a R$199 → 20% | R$200 ou mais → 30%
#Mostre o valor final.

valor_compra = float(input("Digte o valor da compra: "))
if valor_compra < 50:
    print("Sem desconto")
elif valor_compra <= 99:
    print("10% de desconto")
    print("O valor final é: ", valor_compra * 0.9 )
elif valor_compra <= 199:
        print("20% de desconto")
        print("O valor final é: ", valor_compra * 0.8 )
elif valor_compra >= 200:
    print("30% de desconto")
    print("O valor final é: ", valor_compra * 0.7 )