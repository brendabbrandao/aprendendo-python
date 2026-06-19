#Função para calcular juros compostos 

#Na matemática, podemos calcular os juros compostos da seguinte maneira: f(x) == 1000* X 1,13** ^*** X
#* = valor investido 
#** = taxa de 13%
#*** ^= elevado
#X= anos

#%%
def juros_compostos(anos):
    return 1000 * 1.13 ** anos

juros_compostos(4)

#%%
def juros_compostos(aporte, taxa, anos):
    return aporte * (1 + taxa)** anos

juros_compostos(1000, 0.13, 4)    #a ordem altera como executamos uma função

#%%
#Se definir, pode inverter a ordem. A recomendação é manter a ordem e defiir
#os nomes 

juros_compostos(aporte=1000, taxa=0.13, anos=4)

##%%
#Documentar função: 
def juros_compostos(aporte, taxa, anos):
    """
    juros compostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para cálculo do valor a ser retornado
    """
    return aporte * (1 + taxa)** anos

juros_compostos(aporte=1000, taxa=0.13, anos=4)

#Função com string dentro, bem explicadinha - 3 aspas duplas antes e depois
#pra colocar a doc string - e tem que ser desse jeito!

#Dicas do que é esperado em cada um dos elementos da função
#def juros_compostos(aporte:int, taxa:float, anos:int)->float:  - Assim aparece qual tipo é esperado em cada elemento

##%%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:   #nesse caso ele espera retornar um float
    return aporte * (1 + taxa) **anos 