

#métodos - ações que os objetos no python pode ter 

#um dos métodos das listas -> adicionar elementos novos 

# idades = [17, 32, 56, 87]
# print(idades)

#para adicionar um elemento novo nessa lista
# idades.append(42)
# print(idades)

#a própria lista foi modificada adicionando um último elemento no final dela! 


#vou pegar várias idades dos usuários 
idades = []

while True:
    idade = input("Entre com a idade: ")
    if idade == "":
        break
    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("Média: ", media)
print("Mínimo: ", minimo)
print("Máximo: ", maximo)
print("Qtde: ", qtde)

