#como fatiar uma lista? pegar os 4 primeiros elementos 
brenda =['Brenda Brandao', False, '28', 'Noiva', ['Estag', 'Jr', 'Pl', 'Sr', 'Head'], [1, 2, 3, 4] , [1500, 4000, 4500, 6000, 10000] , ['Ana', 'Maria', 'Claudia'] ]
print(brenda[0:4])


#quais foram as duas últimas posições de senioridade? 
print(brenda[4][2:4])

#outra forma de fazer isso
print(brenda[4][-2:]) # vai até o final não precisa pegar o último elemento

# brenda[start : stop : step]  
#start = começo
#stop = fim
#step = qual passo você irá dar

#como navegar na lista de tras pra frente?
salarios = brenda[6]
print(salarios[::-1])