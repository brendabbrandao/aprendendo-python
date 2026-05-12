#Peça a temperatura e diga como está o dia:
#abaixo de 15 → "Frio" | 15 a 25 → "Agradável" | 26 a 35 → "Quente" | acima de 35 → "Muito quente"

temp = input("Insira a temperatura: ") 
temp = float(temp)
if temp < 15:
    print("Frio")
elif temp <= 25:
    print("Agradável")
elif temp <= 35:
    print("Quente")
elif temp > 35:
    print("Muito quente")