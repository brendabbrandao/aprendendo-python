#Exemplo de kwargs 

#Calcular o imposto de um produto 

#Função recebe o preço de venda e o valor do imposto. Vamos supor que existe diferença de imposto dependendo da cidade/estado

def calc_imposto(preco:float, tx_base:float, **kwargs):   #o kwargs é como se fosse um dicionário 
    imposto = preco + tx_base 

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    
    return

calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional=0.001)

print(calc_imposto)