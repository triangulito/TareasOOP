def zipper(x,y):
    xy = ""
    for z in range(len(x+y)):
        if z < len(x):
            xy = xy + x[z]
            if z < len(y):
                xy = xy + y[z]
        elif z < len(y):
            xy = xy + y[z]
        else:
            continue
    print(xy)

def voltear(lista,lista2):
    for x in lista:
        lista2.append(''.join(reversed(x)))
    print(lista2)

x = ("Ernesto")
y = ("Luis")

lista = ["Luis", "Pedro", "Juan"]
lista2 = []
zipper(x,y)
voltear(lista,lista2)