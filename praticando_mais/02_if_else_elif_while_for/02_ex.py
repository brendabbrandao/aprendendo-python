#Peça dois números e uma operação (+, -, *, /). 
# Mostre o resultado. Se a operação não for nenhuma dessas, mostre "Operação inválida".

numero1 = input("Insira o primeiro número: ")
numero1 = float(numero1)
numero2 = input("Insira o segundo número: ")
numero2 = float(numero2)
operacao = input("Insira a operação que você deseja realizar | +, -, *, /: ")


if operacao == "+":
    resultado = numero1 + numero2
    print("Os resultado é: ", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("Os resultado é: ", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("Os resultado é: ", resultado)
elif operacao == "/":
    resultado = numero1 / numero2
    print("Os resultado é: ", resultado)
