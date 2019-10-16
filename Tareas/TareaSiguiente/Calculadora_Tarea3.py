#Tarea 3
def Calculator(string):
    currentChar = "x"
    currentLength = 0
    num = ""
    operationArray = []

    for character in string:
        if currentChar == "x" and character == "x":
            currentLength += 1
            continue
        if currentChar == "y" and character == "y":
            currentLength += 1
            if currentLength == 4:
                operationArray.append(num)
            continue
        if currentChar != character:
            if character == "y":
                if currentLength < 9:
                    num += str(currentLength)
                elif currentLength == 10:
                    num += "0"
                elif currentLength == 11:
                    operationArray.append(num)
                    operationArray.append("+")
                    num = ""
                elif currentLength == 12:
                    operationArray.append(num)
                    operationArray.append("-")
                    num = ""
            elif character == "x":
                if currentLength == 4:
                    operationArray.append(num)
                    continue
            currentChar = character
            currentLength = 1

    num1 = int(operationArray[0])
    num2 = int(operationArray[2])
    op = operationArray[1]

    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    return 0
String = "xyxxxyxxxxxxxxxxxyxxxyxyyyy"
print(Calculator(String))