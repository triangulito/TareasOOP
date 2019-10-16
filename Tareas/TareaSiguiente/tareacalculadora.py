string = input("escribe la operacion = ")
string = list(string)
operacion = []
hola = ["x","y"]
valido = []
for i in range(len(string)):
    letra = string[i]
    if letra  in hola:
        valido.append("si")
    else:
        valido.append("no")
if valido[0] == "si":
    print("numero valido")
    for i in range(len(string)):
        y = string.index("y")
        num = string[:y]
        nume = num.count("x")
        if nume == 10:
            nume = 0
        elif nume == 11:
            nume = "+"
        elif nume == 12:
            nume = "-"
        operacion.append(nume)
        for i in range (y):
            es = num[i]
            quitar = string.remove(es)

        if "x" in string: 
            x = string.index("x")
            nam = string[:x]
            name = nam.count("y")
            if name == 1:
                oo = nam[0]
                quitarr = string.remove(oo)
        else:
            nam = "="
            operacion.append(nam)
            break

    del(operacion[-1])
    operacion = [str(item) for item in operacion]
    operacion = "".join(operacion)

    print (operacion)
    
    g=eval(operacion)
    print("resultado =",g)
    
  
    
else:
    print("no valido")














