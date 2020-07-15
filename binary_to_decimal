# endereço IP - 192.168.1.10
# binario - 1100 0000 1010 1000 0000 0001 0000 1010
# sistema decimal de base 10 - 3785

"""
Três mil    = 3 x 1000      = 3 x 10**3
Setecentos  = 7 x 100       = 7 x 10**2
Oitenta     = 8 x 10        = 8 x 10**1
Cinco       = 5 x 1         = 5 x 10**0
"""

# 3785 = (3*(10**3)) + (7*(10**2)) + (8*(10**1)) + (5*(10**0))
# 3785 = 3x1000 + 7x100  + 8x10   + 5x1
# 3785 = 3000   + 700    + 80     + 5

def bintodecimal(binario):
    base = 8
    potencia = len(binario) - 1
    decimal = 0
    for alg in binario:
        decimal += int(alg)*(base**potencia)
        potencia -= 1
    print('Num em Decimal ', decimal)


def geranum(casas):
    x = 1
    list = []
    c = 0
    while c < casas:
        list.append(x)
        x *= 2
        c += 1
    # retorna listagem ao contrario
    return list[::-1]


def bintodecimal_macete(binario):
    lista = geranum(len(binario))
    print('lista gerada ', lista)
    print('casas ', list(binario))
    decimal = 0
    countLista = 0
    countBinario = 1
    for x in binario:
        if x == '1':
            decimal += lista[countLista]
        countLista += 1
        countBinario += 1
    print(30 * '*')
    print('Num em decimal ', decimal)


bintodecimal_macete('101000')
print(30*'*')
bintodecimal('1257')
