# Crie uma função chamada calcular_area que receba a largura e a altura de um retângulo e retorne a área. 
# Depois peça ao usuário que digite os dois valores e exiba o resultado usando a função.

def calcular_area(largura, altura):
    area = largura * altura
    return area

largura_usuario = float(input("Digite a largura: "))
altura_usuario = float(input("Digite a altura: "))

area_final = calcular_area(largura_usuario, altura_usuario)

print("A área é: ", area_final)