#Função de soma

def soma(a:float, b:float)->float:
    return a + b

def media(a:float, b:float)->float:
    return soma(a, b) /2     #dá pra usar funções dentro de outras funções 

a = float(input("Entre com o valor de A: "))
b= float(input("Entre com o valor de B: "))

print("A média é: ", media(a,b))

#Para colocar mais um argumento (opcional)
def media(a:float, b:float, c=0)->float:   #o argumento opcional tem que vir depois dos argumentos obrigatórios
    return soma(a,b,c) / 3 

#args
def soma(a:float, b:float, *args)->float:   #tudo que passar na função sem ser valor obrigatório o args vai absorver
    valores = [a,b] + args 
    return sum(valores)
