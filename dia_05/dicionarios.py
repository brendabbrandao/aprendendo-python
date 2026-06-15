#Dicionarios = pares de chave/valor  | #Chave que corresponde a um valor (um e apenas um valor associado)

#Como criar um dicionário?
#Inicia com as chaves {}
#1º - chave 
#2º valor
#Separados por vírgula, sempre em parzinho
#As chaves podem ser STRING, INT e FLOAT (esse é mais raro)
#O valor pode ser qualquer tipo

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