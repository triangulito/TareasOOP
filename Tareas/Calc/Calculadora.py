Reglas = {'x':1, 'xx':2, 'xxx': 3, 'xxxx':4, 'xxxxx':5, 'xxxxxx': 6, 'xxxxxxx':7, 'xxxxxxxx':8, 'xxxxxxxxx':9, 'xxxxxxxxxx':'suma', 'xxxxxxxxxx':'resta', 'y':' ', 'yyyy':' '}
num = []
resultado = 0
operación = ''
numy1 = ''
a = input("favor de insertar y en minisculas y x en minisculas: ")
a = list(a)
numtotal = len(a)
for i in range(numtotal):
    if numtotal[i] == 'y':
        spaceholder = None


def Suma(n1, n2):
    resultado = n1 + n2
    return resultado


def Resta(n1, n2):
    resultado = n1 - n2
    return resultado


def CountY(a):
    c = 0
    for i in len(a):
        b = a[i]
        c += 1
        if a != 'x':
            break
    d = a[0:c]
    a.remove(d)
    return d


def CountY(a):
    c = 0
    for i in len(a):
        b = a[i]
        c += 1
        if a != 'y':
            break
    d = a[0:c]
    a.remove(d)
    return d

# x = 1
# xx = 2
# xxx = 3
# xxxx = 4
# xxxxx = 5
# xxxxxx = 6
# xxxxxxx = 7
# xxxxxxxx = 8
# xxxxxxxxx = 9
# xxxxxxxxxx = "suma"
# xxxxxxxxxxx = "resta"
# y = " "
# yyyy = "="