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

left_Rigth1 =str(input("Do you want to go right or left?:\n" )).lower()

if left_Rigth1 == "left":
    swim_wait2 = str(input('You\' have 2 way to swim around the lake or wait for a raft. Please indicate whether to "swim" or "wait".\n')).lower()
    if swim_wait2 =="wait":
        witch_color3 = str(input('On\' the island there are 3 chests of different colors: red, blue and yellow. Does it indicate the color of the chest to try to open it? or ask for help to open them?:\n')).lower()
        if witch_color3 == "yellow":
            print("You Win!!")
        elif witch_color3 =="red":
            print("The red chest exploded when I opened it, you have become ashes. Game over.!! ... Press continue")
        elif witch_color3 =="blue":
            print("You have opened Pandora's box and it is the end of the world. Game over.!! ... Press continue")
        else:
            print("Your treasures have been stolen and you were buried alive. Game over.!! ... Press continue")
    else:
        print("Attacked by lake monsters. Game Over.!! ... Press continue")
else:
    print("You have fallen into a spiked hole. Game over.!! ... Press continue")
