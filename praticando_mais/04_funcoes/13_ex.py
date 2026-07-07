# Crie contar_letras(palavras) que recebe uma lista de strings e retorna um dicionário {palavra: tamanho}. 
# Depois crie palavra_mais_longa(dicionario) que retorna uma tupla (palavra, tamanho) da palavra mais longa. 
# Exemplo: ["python","java","c","javascript"] deve retornar ("javascript", 10).

def contar_letras(palavras):
    resultado = {}
    for palavra in palavras:
        resultado[palavra] = len(palavra)
    return resultado

def palavra_mais_longa(dicionario):
    palavra_maior = ""
    tamanho_maior = 0
    for palavra, tamanho in dicionario.items():
        if tamanho > tamanho_maior:
            tamanho_maior = tamanho
            palavra_maior = palavra
    return palavra_maior, tamanho_maior


palavras = ["brenda", "ernesto", "garrafinha", "tablet", "celular"]

dicionario_letras = contar_letras(palavras)
print(dicionario_letras)

resultado = palavra_mais_longa(dicionario_letras)
print(resultado)