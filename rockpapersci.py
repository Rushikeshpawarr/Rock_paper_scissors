# importing the random library
import random 

# Defining the conditions.
def gameWin(comp, you): 
    if comp == you:
        return None
    elif comp=="r":
        if you=="s":
            return False
        elif you == "p":
            return True
    elif comp=="s":
        if you=="p":
            return False
        elif you=="r":
            return True
    elif comp=="p":
        if you=="r":
            return False
        elif you=="s":
            return True

# Displaying that the computer is working.
print("Comp turn: Rock[r], Paper[p], Scissors[s]?")  
randNo = random.randint(1, 3) # Selecting random numbers between 1 to 3 (Rock, to Scissors)
if randNo == 1:
    comp = "r" # 1 is Rock.
elif randNo==2:
    comp = "p" # 2 is Paper
elif randNo=="3":
    comp = "s" # 3 is Scissor

 # Asking the user input.
you = (input("Your turn: Rock[r], Paper[p], Scissors[s]?"))
a = gameWin(comp, you) # Defining the function in short

# Showing what computer chose.
print(f"Computer chose {comp}") 
print(f"You chose {you}") # Showing what you chose.

if a == None:
    print("The game is tied between you and computer") # Text to be displayed when the game is tied.
elif a:
    print("You won, congrats!") # Text to be displayed when you won.
else:
    print("Computer won, try again..") # Text to be displayed when you lose, the computer won.
