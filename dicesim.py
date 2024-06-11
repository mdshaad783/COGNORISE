import random
import time

def num_sides():
    while True:
        num_sides = int(input("Enter num of sides on dice : "))
        return num_sides
    
def num_rolls():
    while True:
        num_rolls = int(input("Enter num of rolls : "))
        return num_rolls
    
def rolls():
    num_side = num_sides()
    num_roll = num_rolls()
    print(f"Rolling a {num_side} sided dice {num_roll} times")
    for i in range(1,num_roll+1):
        print("Roll ",i,": ",random.randint(1,num_side))
        time.sleep(1)
    play_again = input("Do you want to roll again? (yes/no)\n").lower()
    if play_again == 'yes':
        rolls()
    else:
        print("Thanks for Rolling...:)")
        exit()

if __name__ =="__main__":
    rolls()