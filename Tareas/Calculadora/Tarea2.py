ope = input("Ingresar dato:")
def validacion(ope):
    if "yyyy"not in ope:
        print("you suck!!!")
        return False
    for x in ope:
        if x not in 'xy':
            print("you suck!!!")
            return False
    return True

def calc(ope):
    new = ""
    result =0
    paso2 = ope.split("y")
    if validacion(ope) == True:
        for x in paso2:
            if len(x) == 11:
                x = "+"
            elif len(x) == 0:
                continue
            elif len(x) == 12:
                x = "-"
            elif len(x)== 10:
                x = "0"
            else:
                x = len(x)
            x = str(x)
            new = new+x
        result = eval(new)
        new = new + "="
        print(new, result)

calc(ope)