#Tabuada usando for 

#range é uma estrutura de dados do python que cria uma sequencia de numeros


numero = 2 
max_numero = 100 

for i in range(1, max_numero+1):  #o range vai até o intervalo aberto - ele vai até 99, por isso o +1 | o maior numero menos o primeiro é a quantidade de valores do range
    print(numero, "X", i, "=", numero * i)