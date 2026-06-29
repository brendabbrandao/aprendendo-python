# Crie uma agenda onde cada chave é o nome de um contato e o valor é uma tupla com (telefone, email, cidade). 
# Implemente um menu com as opções: 
# 1 — buscar contato, 
# 2 — listar todos, 
# 3 — sair. 
# Ao listar, exiba os dados formatados.

agenda ={
    "Brenda":("123", "brenda@brenda", "Lorena"),
    "Ernie":("456", "ernie@ernie", "Guara"),
    "trevor":("678", "trevor@gta", "Los Santos")
}

while True:
    menu = int(input("1 - buscar contato | 2 - listar todos | 3 - sair: "))
    if menu == 1:
        buscar = input("Digite o contato que você deseja buscar: ")
        if buscar in agenda:
            telefone, email, cidade = agenda[buscar]
            print(f"{buscar} - Tel:{telefone} Email-{email} Cidade{cidade}")
    elif menu == 2:
        print(agenda)
    else:
        print("Saindo...")
        break

