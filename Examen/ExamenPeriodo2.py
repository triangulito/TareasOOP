class Test:
    def testfunction(self, test):
        if test==True:
            print("true")
        elif test==False:
            print("false")
        else:
            print("else")

str1 = input("String #1: ")
str2 = input("String #2: ")
lst3 = list()

def zipper(str1, str2):
    strR = ""
    # dic = [item for i in zip(lst1, lst2) for item in i]
    if len(str1)>len(str2):
        may = str1
        men = str2
    else:
        may =  str1
        men = str2
    for i in range(len(may)):
        strR += may[i]
        strR += men[i]
    print(strR)


def turn(str1,str2):
    st1R = str1[::-1]
    st2R = str2[::-1]
    print(st1R)
    print(st2R)

zipper(str1,str2)
turn(str1,str2)
