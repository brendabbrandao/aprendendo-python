#Faça um programa que receba dois números e uma operação (+, -, *, /) e exiba o resultado. 

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
operacao = input("Digite a operação (+, -, *, /): ")

numero1 = float(numero1)
numero2 = float(numero2)

if operacao == "+":
    print("Resultado:", numero1 + numero2)

elif operacao == "-":
    print("Resultado:", numero1 - numero2)

elif operacao == "*":
    print("Resultado:", numero1 * numero2)

elif operacao == "/":
    if numero2 == 0:
        print("Erro: não é possível dividir por zero")
    else:
        print("Resultado:", numero1 / numero2)

else:
    print("Operação inválida")
