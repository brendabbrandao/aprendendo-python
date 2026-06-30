# Crie uma função chamada celsius_para_fahrenheit que receba uma temperatura em Celsius e retorne o valor convertido para Fahrenheit. 
# A fórmula é: F = (C × 9/5) + 32. Teste com três temperaturas diferentes.

def celsius_para_fahrenheit(celsius):
   fahrenheit = (celsius * 9/5) + 32
   return fahrenheit

print(f"0º C = {celsius_para_fahrenheit(0)} Fº")
print(f" 22º C = {celsius_para_fahrenheit(22)} Fº")
print(f" 100º C = {celsius_para_fahrenheit(100)} Fº")