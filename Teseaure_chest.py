print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_Rigth =str(input("left or right?: " ))
left_Rigth.lower()

swim_wait = str(input("swim or wait: "))
swim_wait.lower()

witch_color = str(input("Which door, Blue, Red, Yellow: "))
witch_color.lower()

if left_Rigth == "left":
    if swim_wait =="swim":
        print("Attacked by sharp. Game Over.!! ... Press continue")
    elif witch_color == "yellow":
        print("You Win!!")
    elif witch_color =="red":
        print("Burned by fire, you have become ashes.Game over.!! ... Press continue")
    elif witch_color =="blue":
        print("Eaten by beasts. Game over.!! ... Press continue")
    else:
        print("Game over, your saved game will be deleted!!")
else:
    print("You have fallen into a spiked hole. Game over.!! ... Press continue")
