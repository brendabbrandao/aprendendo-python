#Abrindo arquivo
#%%
nome_arquivo = "historia.txt"

# Abre arquivo
open_file = open(nome_arquivo)


# Lê o arquivo
conteudo = open_file.read()

print(conteudo)


# Fecha o arquivo
open_file.close()


#%%

nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file: #outra forma
    conteudo = open_file.read() 

print(conteudo)
