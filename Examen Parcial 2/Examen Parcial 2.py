# 1.-
class Test:
    def testfuction(self, test):
        if True:
            print("true")
        elif False:
            print("false")
        else:
            print("else")


# 2.-

list1 = input("inserta una palabra: ")
list2 = input("inserta una palabra: ")
list1 = list(list1)
list2 = list(list2)
print(list1)
print(list2)


def zipper(a, b):
    c = []
    for i in range(0, max(len(a), len(b))):
        if not a[i-1]:
            c.append(b[i])
        elif not b[i-1]:
            c.append(a[i])
        else:
            c.append(a[i])
            c.append(b[i])
    return c


print(zipper(list1, list2))


# 3.-

def volteado():
    print("para dejar de añadir elementos a la lista inserte 0")
    l = input("inserte cualquier palabra que no sea solo 0")
    while l != '0':
        List1.append(l)
        List2.append(l[:-1])
    print(List1+List2)


print(volteado())

# 4.-
# 4.1 ¿Cual es la primera prgunta donde c es la respuesta correcta? c
# 4.2 ¿Cual es la primera pregunta donde a) es la respuesta correcta?  a
# 4.3 ¿Cual es la primera pregunta donde d es la respuesta correcta?  d
# 4.4 ¿Cual es la primera pregunta donde b es la respuesta correcta? b
