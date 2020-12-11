namelist = []
x = -1

while x != 0:
    x = int(input("Input your number or 0 to exit: "))
    if(x != 0):
        namelist.append(x)
    else:
        break

print(namelist)
