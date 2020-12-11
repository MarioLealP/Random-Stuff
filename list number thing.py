# Empty List
namelist = []
# Do X = Anything but 0
x = -1
# loop for input while x which is the same as the input isn't 0
while x != 0:
    # The Input
    x = int(input("Input your number or 0 to exit: "))
    # Make if so it doesnt append 0 because it only checks for the loop AFTER the append
    if(x != 0):
        # Appends to the list
        namelist.append(x)
    else:
        # Breaks out fo the loop
        break
# Prints the list
print(namelist)
