print ("*******WELCOME TO THE GAME!*******\n")
import random

#Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chooses scissors
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True
    
    # Check for all possibilities when computer chooses paper
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chooses rock
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True

print("Computer's Turn: Choose Rock(r), Paper(p) or Scissors(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Choose Rock(r), Paper(p) or Scissors(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Won!")
else:
    print("You Lost!")
