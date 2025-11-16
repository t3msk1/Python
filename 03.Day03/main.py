
# Background Story
def story():
    print("\n=====Welcome to The Island of Survivor=====\n")
    print("The Island of Survivor is an Island that built to test all of the Knights.\n\nThis Island is full of huge trees and venomous animals, you'll gonna find a other knights and you have to fight with all of your powers.\n\nIF YOU DIE, YOU'll NOT COMING BACK\n\nAND IF YOU WIN, YOUR GONNA MARRY THE PRINCESS")

# Asking permission for user
def permission():
    while True:
        setuju = input("\nAre you ready? (yes/no) " ).lower()
        if setuju == "yes":
            print("\nLet's Start The Game!")
            return True
        elif setuju == "no":
            print("You Can Comeback When You're Ready!")
            return False
        else:
            print("Invalid Input, Try Again!")


# MAIN GAME FLOW
story()
game_start = permission()

# IF IT YES, THEN...
if game_start: 
# Level 1
# Goals: Find the superpower water in the island
    def level1():
        print("\n===== LEVEL 1: THE SHORE =====")
        print("\nYou are waking in the corner of The Survivor Island, the wreckage of your boat scattered around you!.")
        print("You are very thristy and you MUST find water.")
        print("\nIn front of you is a dense of 'Junge'.")
        print("To your 'left', you will see the wreck of a larger ship.")
        print("To your 'right', you see only steep cliffs.")
        
        pilihan1 = input("\nWhere do you wanna go? ").lower()
        if pilihan1 == "left":
            print("\nYou walking toward the large shipwreck...")
            print("There is nothing valuable here except a 'bag' and half-buried 'chest'...")
            choose1 = input("\nWhich one will you open? (bag or chest): ").lower()
            if choose1 == "bag":
                print("\nYou Open the bag and suddenly a venomous snake nesting inside bites your hand!...")
                print("The poison is spread inside your body with unpredicted speed...")
                print("\nYOU CAN'T DO ANYTHING\n===== GAME OVER! =====")
            elif choose1 == "chest":
                print("\nYou dig the chest from the sand...")
                print("You force the chest to open with your power!...")
                print("Inside the chest you find a ruusty dagger, some dry biscuits, and... a leather waterskin that is still FULL!...")
                print("You drink the water and feel that your strength return...")
                print("\n===== CONGRATULATIONS! YOU HAVE PASSED LEVEL 1 =====")
        elif pilihan1 == "right":
            print("\nYou're going to the cliffs...")
            print("Trying to climb the cliffs to get a better view...")
            print("The rocks are very slippery. Your grip one of them and fails...")
            print("And within seconds you fall onto he sharp rocks...")
            print("Your body losing so much blood and...")
            print("Sooner or later your losing your conciousness...")
            print("\nYOU CAN'T DO ANYTHING\n===== GAME OVER! =====")
        elif pilihan1 == "jungle":
            print("\nYou head straight into the dense jungle unprepared...")
            print("You keep going inside the junge...")
            print("You don't notice that YOU'VE BEEN FOLLOWED by another knights...")
            print("They've been waiting your guard down... ")
            print("When that happens they throw a spear through your heart...")
            print("\nYOU CAN'T DO ANYTHING\n===== GAME OVER! =====")
    level1()

# IF IT NO, THEN...
else:
    print("\n===== THANK YOU FOR PLAYING =====")