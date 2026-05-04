#Faça um programa que receba uma temperatura em Celsius e converta para Fahrenheit. A fórmula é: F = C * 1.8 + 32

temp_c = input("Insira a temperratura em Celsius")

temp_c = float(temp_c)

conversao_f = temp_c * 1.8 + 32 

print("A temperatura em Fahrenheit é: ", conversao_f)