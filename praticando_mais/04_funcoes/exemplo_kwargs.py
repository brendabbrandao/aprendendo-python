def calcular(primeiro_numero, segundo_numero, *args, **kwargs):
    # kwargs = { "sorvete": "baunilha", "ernesto": "jose" }
    resultado = 2 * primeiro_numero + segundo_numero
    print('resultado: ', resultado)
    if kwargs["sorvete"]:
        print(f"tem sorvete e é de: {kwargs['sorvete']}")
    return resultado

#operacao_1 = calcular(2, 3)

operacao_2 = calcular(3, 2, 1, sorvete='baunilha', ernesto='jose')


