print("Welcome to the Treasure Island!")
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
 _________|___________| ;`-.o`"=._; ." ` '`.".. . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
)
choice_1 = input("""
*******************************************************
You wash up on the golden sands of a mysterious island. 
Your shipwreck lies smoldering behind you. 
Ahead, a narrow jungle path disappears into thick vines, while the coastline curves toward jagged cliffs. 
A warm breeze carries the faint sound of drums from somewhere inland.
You...
(1) Enter the jungle path
(2) Walk along the cliffs

Your answer: """)

if choice_1 == "1":
    choice_2 = input("""
*******************************************************
The jungle thickens until you reach a fork in the path. 
To the left lies a dark cave emitting a faint metallic clinking—like chains. 
To the right, glowing mushrooms illuminate a winding trail deeper into the forest. 
Strange footprints circle both paths.
You...
(1) Enter the dark cave
(2) Follow the glowing mushroom trail

Your answer: """)
    if choice_2 == "2":
        choice_3 = input("""
******************************************************************************
You arrive at an ancient stone temple, half-collapsed and overgrown with vines. 
In the center sits a pedestal holding a small wooden chest. 
But beside it stands a weathered statue with hollow eyes. 
A faint hum vibrates through the air—magic, alive and waiting.
You... 
(1) Touch the statue
(2) Carefully open the chest
                
Your answer: """)
        if choice_3 == "2":
            print("You uncover the lost treasure of the island—jewels, gold, and the map home.\nYou WIN!")
        else:
            print("The statue springs to life and seals your fate.\nGame Over.")
    else:
        print("A chained beast awakens and devours you in the dark.\nGame Over.")

else:
    print("A sudden rockslide sends you into the sea below.\nGame Over.")