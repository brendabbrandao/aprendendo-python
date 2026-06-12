# Peça um número ao usuário e faça uma contagem regressiva dele até 1, usando for (sem usar while).

contagem = 0
numero = int(input("Digite um número: "))

for i in range(numero, 0, -1):
    print(i)