#Dicionarios = pares de chave/valor  | #Chave que corresponde a um valor (um e apenas um valor associado)

#Como criar um dicionário?
#Inicia com as chaves {}
#1º - chave 
#2º valor
#Separados por vírgula, sempre em parzinho
#As chaves podem ser STRING, INT e FLOAT (esse é mais raro)
#O valor pode ser qualquer tipo, inclusive outros dicionários e listas

dados_teo = {
    "Sobrenome":"Calvo",
    "nome":"Teo",
    "filhos":True,
    "formacao": ["estatistica", "bigdata datascience"],
    "cargos":[
        {"nome": "ds jr", "empresa": "tapps"},
        {"nome": "ds pl", "empresa": "sas"},
        {"nome": "ds sr", "empresa": "boticario"},
        {"nome": "ds espec", "empresa": "via varejo"}
        ]
    } 
#print(dados_teo)

#Como acessar o valor de determinada chave?
#Passa o nome e valor da chave para acessar o resultado
#print(dados_teo["nome"])

#Como descobrir a ultima formação do Teo?
print(dados_teo["formacao"][-1])

#Como o nome da última empresa onde o Teo trabalhou?
print(dados_teo["cargos"][-1]["empresa"])

#Para adicionar mais infos no dicionário, criando uma chave nova
dados_teo["estado civil"] = "casado"
print(dados_teo)

#Como descobrir quais as chaves de um dicionário?
print("Chaves:", dados_teo.keys())

#Como saber os valores de um dicionario?
print("Valores:", dados_teo.values())

#Como trazer os pares chave-valor?
print("Itens: ", dados_teo.items())     #lista de tuplas que tem a chave na primeira posição e o valor na segunda posição


#Como percorrer um dicionário? 
for i in dados_teo:
    print(i, "->", dados_teo[i])

#Outra maneira 
for chave, valor in dados_teo.items:
    print(chave, valor)