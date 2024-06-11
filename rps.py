import random
import time
def user_choice():
    while True:
        user = input("Enter Your Choice : Rock, Paper, Scissor\n").upper()
        return user

def comp_choice():
    comp = random.choice(['ROCK', 'PAPER', 'SCISSOR'])
    return comp

def game_winner(user,comp):
    if user == comp:
        return "The Game is Tie..!!!"
    
    elif user=='ROCK':
        if comp == "SCISSOR":
            return "You Won..!!!"
        elif comp == "PAPER":
            return "You Lost..(:"
        
    elif user=='PAPER':
        if comp == "ROCK":
            return "You Won..!!!"
        elif comp == "SCISSOR":
            return "You Lost..(:"
    
    elif user=='SCISSOR':
        if comp == "PAPER":
            return "You Won..!!!"
        elif comp == "ROCK":
            return "You Lost..(:"
        
def play_game():
    print("***Welcome to Rock-Paper-Scissor Game***\n")
    time.sleep(2)
    user = user_choice()
    comp = comp_choice()

    print(f"You chose {user}\n")
    time.sleep(1)
    print("Computer's turn.....")
    time.sleep(2)
    print(f"Computer chose {comp}\n")
    time.sleep(1)
    result = game_winner(user, comp)
    print(result)
    play_again = input("Do you want to play again? (yes/no)\n").lower()
    if play_again == 'yes':
        play_game()
    else:
        exit()

if __name__ =="__main__":
    play_game()