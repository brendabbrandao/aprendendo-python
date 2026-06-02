# Peça um número ao usuário e faça uma contagem regressiva até zero, exibindo cada número. Ao chegar em zero, exiba "Fim!".


numero = int(input("Digite um número: "))
while numero >=0:
    print(numero)
    numero = numero - 1
print("Fim!")
