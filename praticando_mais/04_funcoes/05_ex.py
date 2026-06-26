# Crie uma função chamada maior_de_idade que recebe uma idade como parâmetro.

# Dentro da função, use if para verificar: se a idade for maior ou igual a 18, imprima "Maior de idade". 

# Senão, imprima "Menor de idade".

def maior_idade(idade):
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")


idade_passada = int(input("Digite sua idade: "))

maior_idade(idade_passada)