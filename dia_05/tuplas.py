#Tuplas = Lista imutável :o

#Para definir uma tupla é preciso colocar [] | Ou não coloca nada

dados_teo = [32, 1, "Casado", "dev golang"]
dados_teo.append("3241.23")
print(dados_teo)

tupla_teo = (2, 1, "Casado", "dev golang")
#tupla_teo = 2, 1, "Casado", "dev golang"]
print(tupla_teo)
print(type(tupla_teo))

#Tentando adicionar um elemento na tupla -> não tem como!!
#tupla_teo.append #não tem!

#E uma lista dentro de tupla? Dá pra alterar a >lista<
tupla_teo_2 = 2, 1, "Casado", "dev golang", ["maria", "antonia"]
tupla_teo_2=[-1].append("Ana")
print(tupla_teo_2)
