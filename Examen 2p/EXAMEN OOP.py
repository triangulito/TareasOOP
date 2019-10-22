# 1.- Corregir el siguiente código valor
class Test:
    def testfunction(self, test):
        if True:
            print("true")
        else:
            print("false")
        #He eliminado el "elif" donde la respuesta se hacia false,
        #debido a que por lo visto se utiliza un operador booleano, por lo que es, o True, o False,
        #por lo que jamás entraria a "else", lo cual lo hace inutil.

# 2.- Hacer una función zipper que reciba dos strings y regrese un string con los caracteres intercalados

def zipper(a,b):
    if len(a)>len(b):
        x=''
        for i in range(len(a)):
            if len(b)>i:
                x+=a[i]+b[i]
            else:
                x+=a[i:]
                print(x)
                break
    else:
        x=''
        for i in range(len(b)):
            if len(a)>i:
                x+=a[i]+b[i]
            else:
                x+=b[i:]
                print(x)
                break
a='Luis'
b='Ernesto'
zipper(a,b)

# 3.- Hacer una función que reciba una lista de strings y regrese una lista con cada una de los strings volteadas
def voltear(a):
    n=''
    for i in range(len(a)-1,-1,-1):
        n+=a[i]
    return(n)

arr=['Luis','Pedro','Juan']
newarr=[]
for i in arr:
    newarr.append(voltear(i))
print(newarr)
    
# 4.- Pregunta extra de opción múltiple
##1d
##2c
##3a
##4b
