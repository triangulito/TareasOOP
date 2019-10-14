import re
class Calculator:
    def calc (self, op):
        y = op.lower().split("y")
        trans = ""
        res = 0
        reg = ""
        for x in y:
            for i in x:
                if i != "x" and "y":
                    raise Exception('Only introduce x or y characters')
            if len(x) > 0 and len(x) <= 9:
                reg += str(len(x))
                trans += str(len(x))
            elif len(x) == 10:
                reg += "0"
                trans += "0"
            elif x == "xxxxxxxxxxx":
                reg += "+"
                trans += "," + "+"
            elif x == "xxxxxxxxxxxx":
                reg += "-"
                trans += "," + "-"
        #ADDING
        z = re.split(',',trans)
        for s in z:
            res += int(s)
        # print(re.split(',',trans))
        print(reg, end="")
        if "yyyy" in op:
            print("=", end="")
            print(res)
        else:
            raise Exception('An equal is necessary to run calculator.')


c = Calculator
c.calc(c,"xxyxxxyxxxxxxxxxxxyxxxxxyxxxyyyy")

c2 = Calculator
c2.calc(c,"xxyxxxyxxxxxxxxxxxyxxxxxyxxxyxxxxxxxxxxxxyxxxxyxxxyyyy")
