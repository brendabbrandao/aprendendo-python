def soma(valor_base, *args):
    # args = (78, 4, 88, 98)
    soma = valor_base
    for item in args:
        soma = soma + item
    print('soma: ', soma)
    return soma

soma(100, 1, 2)
soma(100, 4, 5, 6)
soma(100, 78, 4, 88, 98)