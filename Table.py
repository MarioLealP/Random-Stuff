taulukko = []
otsikot = []

rows = int(input("Anna taulukon rivien määrä: "))
columns = int(input("Anna taulukon sarakkeiden määrä: "))


row = 1
column = 1

for row in range(rows):
    for column in range(columns):
        otsikot.append((row + 5) * 10 / (column + 1))
    taulukko.append(otsikot)
    otsikot = []

print("Anna taulukon sarakkeiden otsikot", str(column+1), "kpl (max 5 merkkiä):")


for column in range(columns):
    print(str(column),":", end=" ")
    otsikot.append(input())

print("Taulukon koko:", rows, "x", columns)

print("Taulukon tyyppi:", type(taulukko))

print("Taulukko otsikoineen tulostettuna:")

for column in otsikot:
    print(column, end="    ")
print("")

for row in range(rows):
    for column in range(columns):
        print(int(taulukko[row][column]), end="    ")
    print("")
