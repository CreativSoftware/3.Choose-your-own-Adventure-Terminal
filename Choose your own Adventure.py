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

print("************************************************************************************************************************************************************************************************************************************************************************************************************************************")

print("You stumble upon a map, this map leads to a treasure that has been sort after for years on end. The treasure could be worth millions.\nYour curiosity gets the better of you so you decide to go after it.")
print("The map leads you to a cave with two entrances. One goes left, the other goes right.")

choice_one = input("Which entrance will you choose? Left or Right?\n")

if choice_one.lower() == "left":
  print("You slip and fall into a large lake. As you tread water You see land not too far away.")
elif choice_one.lower() == "right":
  print("You slip and fall into a hole to your death.\nGAME OVER!\nPLEASE TRY AGAIN")
  exit()
else:
  print("GAME OVER",)
  exit()
  
print("Just when you decide to swim to it, you here a large growl... OMG it sounds Huge!")

choice_two = input("Scared, confused and not knowing where its coming from, you have to make a decision.\nDo you 'Swim to land' or 'Wait'?\n")

if choice_two.lower() == "swim to land":
  print("You swim as fast as you can to land, only to be attacked and killed by a Large Alligator!.\nGAME OVER!\nPLEASE TRY AGAIN")
  exit()
elif choice_two.lower() == "wait":
  print("You wait quietly and patiently until the loud growling noise dissapates into the distance. Then you make your way slowly to land!")
else:
  print("You were pulled under and drowned.\n GAME OVER")
  exit()

print("You walk down deeper into the cave and a hidden door shuts behind. You come accross 3 doors, all different colors.")

choice_three = input("The doors are dirty and faded, but you're able to make out the inscription on each one.\nEach door is labeled a different color, 'Yellow', 'Blue', and 'Red'. Which one do you choose?\n")

if choice_three.lower() == "yellow":
  print("YOU WIN!\nThe Treasure is there for the taking... This door leads you out the cave.\nTHANKS FOR PLAYING!")
elif choice_three.lower() == "red":
  print("When you open the door, a burst of fire hits you, and you burn to death.\nGAME OVER!")
elif choice_three.lower() == "blue":
  print("When you open the door, three large Beasts jump out and kill you.\nGAME OVER!")
else:
  print("You didn't choose any door. You waited too long and suffocated.\nGAME OVER")