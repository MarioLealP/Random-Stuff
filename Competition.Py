from ast import literal_eval
Competition =  {}

CompetitionName = 2

def addresults():
    print("Quit by hitting enter ")
    PlayerName, Results = 2, 2
    while PlayerName != "":
        PlayerName = input("Input Name of the player: ")
        if PlayerName == "":
            break
        Results = input("Results of the player: ")
        Competition[PlayerName] = Results


def printCompetition():
    print("Competition Name:", CompetitionName)
    for key, value in Competition.items():
        print(key, ":", value)


def saveCompetition():
	ComNameTxt = str(CompetitionName) + ".txt"
	f = open(ComNameTxt, "w")
	f.write(str(Competition))
	f.close()



def loadCompetition():
    CompetitionName = input("Input the name of the competition you wish to load: ")
    ComNameTxt = str(CompetitionName) + ".txt"
    loadFile = open(ComNameTxt, "r")
    contents = loadFile.read()
    Competition = literal_eval(contents)
    loadFile.close()
    return CompetitionName, Competition


results = True
while results:
     selection = input ("Enter selection (n - start new, l - load old, s - save, r - results, a - add, q - stop): ")
     if selection == "n" or selection == "N":
         CompetitionName = input("Enter contest name: ")
         Competition =  {}
         # start a fresh competition
         # empties results in competition {}
     elif selection == "l" or selection == "L":
         print ("Load")
         CompetitionName, Competition = loadCompetition()
         # use loadCompetition function
     elif selection == "s" or selection == "S":
         print ("Save")
         saveCompetition()
         # use saveCompetition function
     elif selection == "r" or selection == "R":
         print ("Results")
         printCompetition()
         # use printCompetition function
     elif selection == "a" or selection == "A":
         print ("Add")
         addresults()
         # use addResult function
     elif selection == "q" or selection == "Q":
         break
         #quits the program