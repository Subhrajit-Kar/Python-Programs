import random
import time

dice_faces = {
    1 : "⚀ (1)" ,
    2 : "⚁ (2)" ,
    3 : "⚂ (3)" ,
    4 : "⚃ (4)" ,
    5 : "⚄ (5)" ,
    6 : "⚅ (6)"
}

def dice_rolled():
    print("\tYou've rolled the dice...")
    time.sleep(2)
    num = random.randint(1, 6)
    face = dice_faces[num]
    print("\tYou've rolled a", face, "!!")

while True:
    temp = input("Do you want to roll the dice again (Y/N) : ").upper()
    if temp == "Y" :
        dice_rolled()
    elif temp == "N" :
        print("Thanks for playing!!!")
        break
    else:
        print("Invalid Input! Please enter between 'Y' or 'N' ")
    