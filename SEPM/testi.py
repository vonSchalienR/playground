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
    if computer == 3:
           print("Computer won. Parempi onni ens kerralla!")
    else:
        print("You won. WOHOO!")

def tilanneTiedotus(user, computer):
    print()
    print("***Situation***")
    print("You:", user)
    print("Computer:", computer)
    print()

# Computer's "random" choice...
def computer_choice(choices):
    return random.choice(choices)

def help():
    print("Welcome to HELP")
    print("Kyl sä nyt KSP osaat ;)")
    print("Help finished.")

def play_game():
    # user and computer wins     
    user_wins = 0
    computer_wins = 0

    # Print out something
    print("Let's play rock paper scissors!")
    print("Type help if you need to see the rules.")
    print("Type Q for quit.\n")

    # Repeat game until game is over.
    while user_wins < 3 and computer_wins < 3:
        user_input = "null"
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        
        user_input = input("Tee valintasi (rock, paper, scissors, lizard, Spock): ")

        if user_input.lower() == 'q':
            print("Quitting game.")
            return

        if user_input.lower() == 'help':
            help()
            continue
        
        # Computer's "random" choice...
        computer_chose = computer_choice(choices)
        
        print(f"\nYou chose {user_input}, computer chose {computer_chose}.\n")

        # Check who wins a round or if it is a tie    
        if user_input == computer_chose:
            print(f"Both players selected {user_input}. It's a tie!")
            tilanneTiedotus(user_wins, computer_wins)

        elif (user_input, computer_chose) in [("rock", "scissors"), ("rock", "lizard"), ("paper", "rock"), ("paper", "Spock"),
                                              ("scissors", "paper"), ("scissors", "lizard"), ("lizard", "Spock"),
                                              ("lizard", "paper"), ("Spock", "rock"), ("Spock", "scissors")]:
            print(f"{user_input.capitalize()} beats {computer_chose}. You win!")
            user_wins += 1
            tilanneTiedotus(user_wins, computer_wins)

        else:
            print(f"{computer_chose.capitalize()} beats {user_input}. Computer wins!")
            computer_wins += 1
            tilanneTiedotus(user_wins, computer_wins)
                
    # Announce winner     
    winner(user_wins, computer_wins)

play_game()
