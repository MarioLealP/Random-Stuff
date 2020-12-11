FName = input("1st Name: ")

SName = input("2nd Name: ")

TName = input("3rd Name: ")

if (FName != SName):
    if (FName != TName):
        if (SName != TName):
            if (FName > SName):
                FName, SName = SName, FName
            if (FName > TName):
                FName, TName = TName, FName
            if (SName > TName):
                SName, TName = TName, SName
            print("Sorted Alphabetically: ", FName, SName, TName)
        else:
            if (FName > SName):
                FName, SName = SName, FName
            print("Sorted Alphabetically: ", FName, SName)
    else:
        if (FName > SName):
            FName, SName = SName, FName
        print("Sorted Alphabetically: ", FName, SName)
else:
    if (FName > TName):
        FName, TName = TName, FName
    print("Sorted Alphabetically: ", FName, TName)
