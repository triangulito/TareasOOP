class Test:
    def testfunction(self, test):
        if test == True:
            print("true!")
        elif test == False:
            print("false!")
        else:
            print("else")

def zipper(s1, s2):
    i = 0
    finalString = ""
    while (i < len(s1)):
        finalString = finalString + s1[i] + s2[i]
        i = i + 1
    return finalString
s1 = "LOLA"
s2 = "BABY"
print(zipper(s1,s2))

def flip(lista):
    x = ""
    for i in range(len(lista)-1,-1,-1):
        x += lista[i]
    print(x)

lista = ["Fulano","Mengano"]
print(flip(lista[0]+ lista[1]))


#Parte 4
#1. a
#2. d
#3. c
#4. b
