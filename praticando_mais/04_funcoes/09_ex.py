# Crie uma função chamada saudacao que recebe um parâmetro nome e retorna (não use print dentro da função)
#  a string "Olá, {nome}! Bem-vindo(a).". Depois, chame a função e imprima o resultado fora dela.

def saudacao(nome):
    return f"Olá {nome}! Bem vindo(a)"

resultado = saudacao("brenda")
print(resultado)