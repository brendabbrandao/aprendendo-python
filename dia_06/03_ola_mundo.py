#Criando uma função que irá exibir uma saudação 

#Essa função não retorna nada

#%%
#Escopo da função = corpo da função | variáveis ali dentro são do escopo da função
def ola_mundo():
    msg= ("Boas vindas para você!")  #não é possível usar essa variável fora da função
    print(msg)

ola_mundo()