def valid(entrada):
    a='xy'
    for i in entrada:
        if i not in a:
            return False
    return True

def calc(entrada):
    t=''
    datos=entrada.split('y')
    for i in range(len(datos)):
        x=str(len(datos[i]))
        if x=='11':
            x='+'
        elif x=='12':
            x='-'
        elif x=='0':
            continue
        t+=x
    print(eval(t))
    
dato=input("\t\tCalculadora de X's y Y's\nIngrese su dato: ").lower()

if valid(dato)==True:
    calc(dato)
else:
    print('El dato ingresado no cumple con las caracteristicas')
