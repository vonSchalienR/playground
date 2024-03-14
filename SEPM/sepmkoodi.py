#File created 20201203 8:58 GMT+2
import random

# Game ends when player or computer wins three times.
def GameOver(user,computer):

    if user==3 or computer==3:
        
        return True
    
    else:

        
        return False

# Some comment here       
def winner(computer, user):

    print("Game over!")
    
    if user == 3:
        print("You won. Wuhuu!")
    else:
        print("Computer won. parempi onni ens kerralla!")


def tilanneTiedotus(user, computer):
    print()
    print("***Situation***")
    print("You:", user)
    print("Computer:", computer)
    print()

# Computer's "random" choice...
def computer_choice(choices):

    return random.choice(choices)

# TODO: continue here
#def help():
#    print("Help missing")

def play_game():
    # user and computer wins     
    user_wins = 0
    computer_wins = 0
    rounds = 0

    # Print out something
    print("Let's play rock paper scissors!")
    print("Type help if you need to see the rules.")
    print("Type Q for quit.\n")

    # Repeat game until game is over.
    while rounds < 3:

        user_input = "null"
        choices = ["rock", "paper", "scissors", "lizard", "spock"]

         
        user_input = input("Tee valintasi (rock, paper, scissors, lizzard, Spock): ")
        



        # Computer's "random" choice...
        computer_chose = computer_choice(choices)
        
        print(f"\nYou chose {user_input}, computer chose {computer_chose}.\n")

        # Check who wins a round or if it is a tie    
        if user_input == computer_chose:
            
            print(f"Both players selected {user_input}. It's a tie!")
            tilanneTiedotus(user_wins, computer_wins)

        elif user_input == "rock":
            
            if computer_chose == "scissors":
                print("Rock smashes scissors! You win!")
                user_wins += 1
                tilanneTiedotus(user_wins, computer_wins)

            elif computer_chose == "Spock":
                print("Spock vaprizes Rock! You lose!")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)

            elif computer_chose == "lizzard":
                print("Kivi murskaa liskon! You win!")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)                

            else:
                print("Paper covers rock! todo, who wins.")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)

        elif user_input == "paper":
            
            if computer_chose == "rock":
                print("Paper covers rock! You win!")
                user_wins += 1
                tilanneTiedotus(user_wins, computer_wins)

            elif computer_chose == "Spock":
                print("Paper disproves spcok! You win!")
                user_wins += 1
                tilanneTiedotus(user_wins, computer_wins)

            elif computer_chose == "lizard":
                print("Lizard eats paper! You lose!")
                computer_wins += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)
                
        elif user_input == "scissors":

            if computer_chose == "paper":
                print("Scissors cuts paper! You win!")
                user_wins += 1
            elif computer_chose == "Spock":
                print("Spock smashes Scissors! You lose!")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)
            elif computer_chose == "lizzard":
                print("Scissors decapitates Lizzard! You win!")
                user_wins += 1
                tilanneTiedotus(user_wins, computer_wins)


                
            else:
                print("Rock smashes scissors! You lose.")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)

        elif user_input == "lizard":
            if computer_chose == "Spock":
                print("Lizard poisons Spock! You win!")
                user_wins += 1


            elif computer_chose == "rock":
                print("Rock crushes lizzard! You lose, buuhuu!")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)
            elif computer_chose == "paper":
                print("Lizard eats paper! You win!")
                user_wins += 1
                tilanneTiedotus(user_wins, computer_wins)
            else:
                print("Scissors decapitates Lizard! You lose!")
                computer_wins += 1
                tilanneTiedotus(user_wins, computer_wins)
        rounds+=1
                
    # Announce winner     
    winner(user_wins, computer_wins)


play_game()
