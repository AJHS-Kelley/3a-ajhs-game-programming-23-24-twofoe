# Pick the secret number from a range for the possible numbers (i.e 0-10, 0-100, 100-200)
# Provide the player X number of guessess, based on range of numbers
# Player needs to guess a number 
# Compare guess to secret number 
# If the guess is correct what should happen?
    # Award the player a point 
    # Print a 'win' message on the screen 
# If the guess is incorrect, what schould happpen?
    # Indicate if guess is high or low compared to secret number 
# If the player does not guess correctly before hitting limit, what happens?
    # Award a point to the cpu
    # Print a loss message 
# First player to score at least 3 points deleared the winner 
    
# You need to add the code to select a difficulty level! 
# Guess a Number, Zac Scott, v0.0
import random, tracemalloc, winsound
from PIL import Image
tracemalloc.start()

# DECLARATIONS
scretNumber = 3 # Range: 0 -- 10
playerName = "" # empty string
playerScore = 0
cpuScore = 0
numGuesses = 0
playerGuess = -1
difficulty = None
numAttempts = None
rangeMin = -1
rangeMax = -1

loserSound = 'sfx/numberGuess/gameOver.wav'
winnerSound = None

imageWin = Image.open('img/numberGuess?win.jpg')
imageLoss = Image.open('img/numberGuess?loss.jpg')


print("""
        +===================================+
        |                                   |
        |          Guess the number         |
        |                by                 |
        |            Zachariah S.           |
        |               2024                |
        +===================================+
        """)    
        
playerName = input("What should i call you?\nType your name and press enter.\n")
# VEFIFY INPUT WHENEVER POSSIBLE!
print(f"You want me to call you {playerName}. Is that correct?")
isCorrect = input("Please type yes if correct, no if not correct.\n")
if isCorrect == "yes" :
    print(f"ok {playerName}, let's continue!")
else:
    playerName = input("What should i call you?\nType your name and press enter.\n")

# PLAYER GUESS
print("you need to guess a number from 0 to 20. you have four gusses!\n")

while playerScore != 3 and cpuScore != 3:
    #pass Tells Python to skip this block without giving an error.
    secrectNumber = random.randint(0, 20) # INCLUSIVE
    #print(secretNumber)
    print(f"Player score: {playerScore}\nCPU Score: {cpuScore}\n")
    numGuesses = 0
    for guesses in range (4):
        print(f"You have {4 - numGuesses} guesses left this round!\n")
        playerGuess = int(input("Think of your number, typr it in and then push ENTER.\n"))
        #int() converts whatever is input into an INTERGER
        print(f"You have picked {playerGuess}. Let's see if it is a match!\n")
        if playerGuess == secrectNumber:
            playerScore += 1
            print("A winner is you! It's a match!\n")
            break # immediately exit a loop!
        else:
            if playerGuess < secrectNumber: 
                print("Your guess is too low!\n")
            else:
                print("Your guess is too high!\n")
        numGuesses += 1
        
    if playerGuess != secrectNumber:
        print("You did not guess correctly before running out of gesses, the CPU won")
        winsound.PlaySound(loserSound, winsound.SND_FILENAME)
        cpuScore += 1
    


if playerScore >= 3:
    print("You scored three points first, well done!")
    imageWin.show()
else:
    print("The CPU has scored three points first and defeated you.")
    imageLoss.show()

    print("Memory Usage: (Current, Peak)")
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()