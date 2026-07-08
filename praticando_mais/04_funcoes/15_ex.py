# Crie uma função chamada agrupar_por_categoria(produtos) que recebe uma lista de tuplas no formato (nome_produto, categoria, preco)
#  e retorna um dicionário onde cada chave é uma categoria, 
# e o valor é uma lista com os nomes dos produtos daquela categoria. 
# Em seguida, crie uma segunda função categoria_mais_cara(produtos) que recebe a mesma lista de tuplas 
# e retorna uma tupla (categoria, soma_precos) da categoria que somou o maior valor total em preços. 
# Exemplo de entrada: [("caneta", "papelaria", 2.5), ("caderno", "papelaria", 15.0), ("mouse", "eletronicos", 45.0), ("teclado", "eletronicos", 80.0)]

def agrupar_por_categorias(produtos):
    agrupado = {}
    for nome_produto, categoria, preco in produtos:
        if categoria not in agrupado:
            agrupado[categoria] = []
        agrupado[categoria].append(nome_produto)
    return agrupado

def categoria_mais_cara(produtos):
    soma_por_categoria = {}
    for nome_produto, categoria, preco in produtos:
        if categoria not in soma_por_categoria:
            soma_por_categoria[categoria] = 0 
        soma_por_categoria[categoria] += preco

    categoria_vencedora = ""
    maior_soma = 0
    for categoria, soma in soma_por_categoria.items():
        if soma > maior_soma:
            maior_soma = soma
            categoria_vencedora = categoria
    return categoria_vencedora, maior_soma

produtos = [
    ("caneta", "papelaria", 2.5),
    ("caderno", "papelaria", 15.0),
    ("mouse", "eletronicos", 45.0),
    ("teclado", "eletronicos", 80.0)
]

print(agrupar_por_categorias(produtos))
print(categoria_mais_cara(produtos))

