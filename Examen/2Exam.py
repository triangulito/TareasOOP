# 1. Corregir el siguiente código:
#class Test
#    function testfunction(self, test):
#        if true:
#            print("true")
#        elseif false:
#            print("false")
#        else:
#        print("else")


# Corrección


class Test:
    test = True

    def __init__(self, test):
        self.test = test
        if test:
            return "true"
        elif test:
            return "false"
        else:
            return "else"

    print(test)

# 2. Hacer una función "zipper" que reciba 2 strings y regrese un string con los caracteres intercalados:
# Ejemeplo: "Luis" "Eernesto" | sR = "LEurinsesto"


def words(w1, w2):
    l1 = list(w1)
    l2 = list(w2)
    w3 = zip(l1, l2)

    return w3


print(words("Luis", "Ernesto"))


# 3. Hacer una función "voltear" que reciba una lista de strings
# y regrese la misma lista pero con los strigs volteados.
# Ejemplo: ["Luis", "Pedro", "Juan"]
#          ["siuL", "ordeP", "nuaJ"]


def swap(li):
    swapped = []
    for str in li:
        str[::-1]
        return str


print(swap(["Luis", "Pedro", "Juan"]))

# 1. c)
# 2. b)
# 3. d)
# 4. b)