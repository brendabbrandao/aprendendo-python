# Faça um programa que pergunte o ano de nascimento da pessoa e calcule quantos anos ela tem (considerando o ano atual como 2025)


ano_nascimento = input("Insira o ano em que você nasceu: ")

ano_nascimento = int(ano_nascimento)

idade = 2025 - ano_nascimento

print("Você tem: ", idade, "anos")