
def power(a,b):
    if b == 0:
        return 1
    elif b != 0:
        if a == 0:
            return 0
        elif a == 1:
            return 1
        elif (a != 1) or (a != 0):
            if b == 1:
                return a
            elif b != 1:
                return a * power(a,b-1)

print(power(2,2))
