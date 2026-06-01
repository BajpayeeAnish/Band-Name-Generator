print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You are at a crossroad, you need to choose which way to go!")
first_choice = input("You must go Left or Right - to choose left type l and to choose right choose r ")
if first_choice == 'l':
    print("You have come inFront of a sea. You must choose to swim or wait near the shore. ")
    second_choice = input("Choose s for swim and w for wait.")
    if second_choice == 'w':
        print("A boat arrived and you sailed to an island. Now there are three doors in front of you.")
        third_choice = input("There are Red, Yellow, Blue doors in front of you. Choose r for Red, y for Yellow, b for Blue.")
        if third_choice == "y":
            print("Hooray!!! You win!! You found the treasure. ")
        elif third_choice == "r":
            print("Game Over!!! You were burned by fire.")
        elif third_choice == "b":
            print("Game Over!!! You were eaten by beasts.")
        else:
            print("Game Over!!!!")
else:
    print("Fall into a hole. Game Over!!!")
