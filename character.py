
tuplostest1 = (0,0)
tuplostest2 = (0,0)
tuplostest3 = (0,0)



attackOne,defenseOne = tuplostest1
attackTwo,defenseTwo = tuplostest2
attackThree,defenseThree = tuplostest3


playerOne =  str(input("Player 1 : "))
attackOne = int(input("atk: "))
defenseOne = int(input("def: "))

playerTwo =  str(input("Player 2 : "))
attackTwo = int(input("atk: "))
defenseTwo = int(input("def: "))

playerThree = str(input("Player 3 : "))
attackThree = int(input("atk: "))
defenseThree = int(input("def: "))

tuplostest1 = (attackOne, defenseOne)
tuplostest3 = (attackTwo, defenseTwo)
tuplostest2 = (attackThree, defenseThree)


players = [
[playerOne, tuplostest1],
[playerTwo, tuplostest2],
[playerThree, tuplostest3]
]


print(players)

if(attackOne > attackTwo and attackOne > attackThree):
    print("Ataque " + str(playerOne) + " " + str(attackOne))
if(attackTwo > attackOne and attackTwo > attackThree):
    print("Ataque " + str(playerTwo) + " " + str(attackTwo))
if(attackThree > attackOne and attackThree > attackTwo):
    print("Ataque " + str(playerThree) + " " + str(attackThree))
if(defenseOne > defenseTwo and defenseOne > defenseThree):
    print("Defesa " + str(playerOne) + " " + str(defenseOne))
if(defenseTwo > defenseOne and defenseTwo > defenseThree):
    print("Defesa " + str(playerTwo) + " " + str(defenseTwo))
if(defenseThree > defenseOne and defenseThree > defenseTwo):
    print("Defesa " + str(playerThree) + " " + str(defenseThree))