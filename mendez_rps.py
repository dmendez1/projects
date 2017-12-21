#David Mendez

#Rock Paper Scissors 
#import random
import random
#constants
player_wins = 0
computer_wins = 0
#make a nice header with *
print ("*" * 20)

print ("Welcome to The Rock Paper Scissor Game!")

print ("*" *20)
#create while statement
while computer_wins < 4 and player_wins <4:
    computer_choice = int(random.randint(0,2))

    player_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors:"))
#create if statements

    if player_choice == 0 and computer_choice == 0:
        print("You both chose Rock, it's a tie! Wow you tied a computer..")
#when computer chooses 0 and you choose 0 its a tie.

    elif player_choice == 1 and computer_choice == 0:
        print("Paper beats rock, good job you can beat a computer.")

        player_wins = player_wins + 1
#when player chooses1 and computer chooses 0 you win.

    elif player_choice == 2 and computer_choice == 0: 
        print("Rock beats paper! Good job!")

        player_wins = player_wins + 1
#when you choose 2 and computer chooses 0 player wins

    elif player_choice == 0 and computer_choice == 1:
        print("Paper covers rock, you suck at this.")

        computer_wins = computer_wins + 1
#when you choose 0 and compuiter chooses 1 computer wins.

    elif player_choice == 1 and computer_choice == 1:
        print("Paper vs paper, it's a tie!")
#when computer chooses 1 and you choose 1 its a tie.        

    elif player_choice == 2 and computer_choice == 1:
        print("Scissors cut paper! You win!.")

        player_wins = player_wins + 1
#when you choose 2 and the computer chooses 1 you win.

    elif player_choice == 0 and computer_choice == 2:
        print("Rock beats Scissors! You win!")

        player_wins = player_wins + 1
#when you choose 0 and the computer chooses 2 you win.

    elif player_choice == 1 and computer_choice == 2:
        print("Scissors cut paper, you lose!")

        computer_wins = computer_wins +1           
#when you choose 1 and computer chooses 2 comuter wins.

    elif player_choice == 2 and computer_choice == 2:

        print("Scissors vs Scissors, you tie!")
#when computer chooses 0 and you choose 0 its a tie.        

print("*" * 20)
#print outro heade

if computer_wins == 4:
            print("Wow you let a computer win %d to %d." % (computer_wins, player_wins))
if player_wins == 4:
            print("You lucked out, you won! %d to %d" % (player_wins, computer_wins))
            print("*" *20)
#make if statements for the end of tournament results.        
print("*" *20)
        
        


    

	
