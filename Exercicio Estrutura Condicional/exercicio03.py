import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

numero = input('Digite um valor: ')


if numero.isdigit:
    numero = int(numero)
    if numero % 2 == 0:
        print("Par")
    else:
        print('Impar')
else:
    print("Isso não e um numero valido")

