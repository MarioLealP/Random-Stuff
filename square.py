def readNumber():
     number = input("Give a Number: ")
     while True:
         if number.lstrip("+-").isdigit():
             return number
         else:
             number = input("Give a Number: ")

n = float(readNumber())
print (n * n)