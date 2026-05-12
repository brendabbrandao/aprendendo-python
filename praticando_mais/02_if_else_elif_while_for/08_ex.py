#O usuário tem 3 tentativas para digitar a senha correta ("python"). 
#Se acertar, mostre "Bem-vindo!". Se esgotar as tentativas, mostre "Conta bloqueada."


tentativas = 3 
senha = ""

while tentativas > 0 and senha != "python":
    senha = input("Digite uma senha: ")
    if senha != "python":
        tentativas = tentativas -1
        print("Senha errada. Você tem:", tentativas, "restantes")
    if senha == "python":
        print("Bem-vindo!")
    else:
        print("Conta bloqueada")