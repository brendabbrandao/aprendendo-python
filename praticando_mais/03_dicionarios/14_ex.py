# Você tem um dicionário agenda com nomes e telefones já cadastrados:

# Peça ao usuário um nome. Se o nome estiver na agenda, exiba o telefone. Se não estiver, imprima "Contato não encontrado."

agenda = {
    "Ana": "99111-2233", ""
    "Bruno": "98877-6655", 
    "Carla": "97654-3210"
    }

while True:
    nome = input("Digite um nome: ")
    if nome != "":
        break

info = agenda.get(nome)

if info =="":
    print("Contato não encontrado")
else:
    print("Nome: ", nome, "telefone: ", agenda[nome])