#ejercicio1
class Test:
    def __init__(self, test):
        self.test = test
        if True:
            print("true")
        elif False:
            print ("false")
        else:
            print("else")
#ejercicio2
def zipper(string1, string2):
    finalstri = ""
    for i in range(len(string1)):
        finalstri = finalstri + string1[i] + string2[i]

    return (finalstri)


string1 = "Luis"
string2 = "Ernesto"
print(zipper(string1, string2))
#ejercicio2 intenete este codigo profe
def zipper(string1, string2):
    x = len(string1)
    y = len(string2)
    finalstri = ""
    for i in range(len(string1)):
        finalstri = finalstri + string1[i] + string2[i]
        largo = y - x
    return (finalstri)
    rest = string2[largo]
    resultado = finalstri + rest
    return (restlado)


string1 = "Luis"
string2 = "Ernesto"
print(zipper(string1, string2))
#ejercicio3
def voltear(lista):
    imprimir = []
    for i in range (len(lista)):
        caracter = lista[i]
        caracter = list(reversed(caracter))
        imprimir.append(caracter)
    return(imprimir)

lista = ["Luis", "Pedro", "Juan"]
print(voltear(lista))

#ejercicio 3, segunda opcion
def voltear(lista):
    imprimir = []
    for i in lista:
        imprimir.append(list(reversed(i)))
    return(imprimir)

lista = ["Luis", "Pedro", "Juan"]
print(voltear(lista))


#ejercicio4
#1-a
#2-c
#3-d
#4-b
