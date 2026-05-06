#Quais  números são divisíveis por 4 num intervalo de 4 até 100?


count = 4 

while count <= 100: 
    resto = count % 4 
    if resto == 0:
        print(count)
    count += 1