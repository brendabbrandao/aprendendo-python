# Crie uma lista com 5 frutas. Peça ao usuário uma fruta e informe se ela está ou não na lista.



frutas = ["Maça", "Banana", "Laranja", "Limao", "Morango"]

fruta = input("Digite uma fruta: ") 

if fruta in frutas:
    print("Essa fruta está na lista!")
else:
    print("Essa fruta não está na lista!")
