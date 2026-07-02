# Função é uma caixa preta que irá executar um código - por isso é importante nomear certinho 

# Parametro -> é como se fosse o valor x da equação (o x pode ser qualquer número)

a = 1
b = 2
c = 3
d = 4

def soma_especial(x, y):
    return x + y

def soma_a_b():
    global soma
    soma = a + b

# 1. somar a + b
soma_1 = soma_especial(2, 1)
print('soma 1: ', soma_1)

# 2. somar c + d
soma_2 = soma_especial(c, d)
print('soma 2: ', soma_2)

# 3. somar a + d
soma_3 = soma_especial(a, d)
print('soma 3: ', soma_3)

# 4. somar b + c
soma_4 = soma_especial(b, c)
print('soma 4: ', soma_4)

soma_a_b()
print('soma 5: ', soma)