#Função de soma

def soma(a:float, b:float)->float:
    return a + b

def media(a:float, b:float)->float:
    return soma(a,b)/2     #dá pra usar funções dentro de outras funções 

a = float(input("Entre com o valor de A: "))
b= float(input("Entre com o valor de B: "))

print(media(a,b))