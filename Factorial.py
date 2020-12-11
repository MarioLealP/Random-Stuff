def printNumberNumber(O, F):
    print(O, "! = ", F)


def readInteger():
        inte = input("Enter integer: ")
        try:
            x = int(inte)
            return(int(x))
        except ValueError: 
            print("It's not a number")
            return "false"

def CalculateMultiplier(n):
    fact = 1
    for i in range(n+1): 
        fact = fact * i 
    return(fact)





OriginalNumber = 0

while OriginalNumber >= 0:

    OriginalNumber = readInteger()
    
    while OriginalNumber == "false":
        OriginalNumber = readInteger()

    if OriginalNumber < 0:
        break

    FactorialNumber = CalculateMultiplier(OriginalNumber)
    printNumberNumber(OriginalNumber, FactorialNumber)

print("Leaving this thing behind")