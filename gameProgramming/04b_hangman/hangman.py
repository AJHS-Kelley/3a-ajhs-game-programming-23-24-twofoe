import random 
wordList = 'deal bill real steal less best test rest desk perk work dirt turn bro will teal lee bee tea chicken football sports fat lunch school middle low black blue sea'.split()
#.split() will split a string into separate elements, by default based on SPACE

# VARIABLE_NAMES that are ALL CAPS AREE CONSTANTS and not meant to change
HANGMAN_BOARD = ['''
    +----+
         |        
         |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
         |        
         |        
         |        
       =====''', '''   
    +----+
    O    |        
    |    |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
    |\   |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
   /|\   |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
   /|\   |        
     \   |        
         |        
       =====''', '''
    +----+
    O    |        
   /|\   |        
   / \   |        
         |        
       =====''']

def getRandomWord(wordList):
    wordIndex = random.randint(0 , len(wordList) - 1)
    # len(listName) - 1 is most common way to prevent index out of range errors
    # print(wordIndex)
    return wordList[wordIndex]

def displayBoard(incorrectLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(incorrectLetters)])
    print()

# i = 0
# while i < 10:
#    getRandomWord(wordList)
#    i += 1 