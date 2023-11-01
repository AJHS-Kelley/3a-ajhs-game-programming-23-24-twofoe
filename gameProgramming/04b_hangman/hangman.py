import random 
wordList = 'deal bill real steal less best test rest desk perk work dirt turn bro will teal lee bee tea chicken football sports fat lunch school middle low black blue yellow red white green brown coast jackson mandarin sandalwood bault westside flecter'.split()
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

def get

# i = 0
# while i < len(HANGMAN_BOARD):
#    print(HANGMAN_BOARD[i])
#    i += 1 