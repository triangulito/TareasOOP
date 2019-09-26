def tar(num1, num2):
    a = num2
    if num1 == 0:
        return 0
    elif num1 != 0:
        return tar(num1**a, num2*1)

def fib(num):
    if num <= 1:
        return num
    else:
        return (fib(num-1)+fib(num-2))

print(fib(7))