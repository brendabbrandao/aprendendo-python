# Crie um dicionário semana onde a chave é um número de 1 a 7 e o valor é o nome do dia correspondente. Exemplo: 1 → "Segunda-feira".

# Peça ao usuário um número. Se estiver entre 1 e 7, imprima o dia. Se não estiver, imprima "Número inválido."

dias_da_semana={
    1:"Domingo",
    2:"Segunda-feira",
    3:"Terça-feira",
    4:"Quarta-feira",
    6:"Quinta-feira",
    7:"Sexta-feira"
    
}

numero = int(input("Digite um número: "))

if numero in dias_da_semana:
    print("O dia da semana é: ", dias_da_semana[numero])
else:
    print("Número inválido")
    