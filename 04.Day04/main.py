# Rock, Paper, Scissors

import random
choices = ["Rock", "Paper", "Scissor"]
#index = [0, 1, 2]

# Greetings
def greet():
    print("\n===== WELCOME TO THE GAME =====")

# Ready?
def permission():
    while True:
        setuju = input("\n===== ARE YOU READY TO PLAY? (yes/no) =====\n\n").lower()
        if setuju == "yes":
            print("\n=====Let's Start The Game=====")
            return True
        elif setuju == "no":
            print("\nYou Can Comeback Later")
            return False
        else:
            print("Invalid Input, Retry!")

# Cooking
def player_choices():
        while True:
            try: 
                choice_player = int(input("\nChoose between 0 for Rock, 1 for Paper, 2 for Scissor "))
                if 0 <= choice_player <= 2:
                    player_pick = choices[choice_player]
                    print(f"You Choose a {player_pick}")
                    return player_pick #Mengirimkan hasil ke player_pick
                else:
                    print("Choose the Right one, Retry!")
            except ValueError:
                print("Invalid Input, Retry!")

# Cooking
def computer_choices():
        cpu_pick = random.choice(choices)
        print(f"Computer Choose a {cpu_pick}")
        return cpu_pick # Mengirimkan hasil ke cpu_pick

# Using
def finalwinner(player_pick, computer_pick):
    print(f"\n===== {player_pick} VS {computer_pick} =====")
    if player_pick == computer_pick:
        print("\n===== DRAW! =====")
    elif (player_pick == "Rock" and computer_pick == "Scissor") or \
         (player_pick == "Paper" and computer_pick == "Rock") or \
         (player_pick == "Scissor" and computer_pick == "Paper"):
        print("\n===== YOU WIN! =====")
    else:
        print("\n===== YOU LOSE! =====")

# MAIN GAME!
greet()
game_start = permission()

if game_start:
    p_choice = player_choices() #player_choice depending on player_pick
    c_choice = computer_choices() #computer_choice depending on cpu_pick
    finalwinner(p_choice, c_choice)
else:
    print("\n===== GAME OVER! =====")