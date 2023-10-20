# # ADDING ITEMS
# playerInventory = []
# while len(playerInventory) < 10:
#     item = input("What do you want to add?\n")
#     playerInventory.append(item) # .append() adds to END of list.
# playerInventory.sort()
# # .whatever() is known as a METHOD. It means "do this to that".
# print(playerInventory)

# # REMOVE ITEMS
# while len(playerInventory) > 5:
#     item = input("What do you want to add?\n")
#     playerInventory.remove(item)
# playerInventory.sort()
# print(playerInventory)

# FIXED INVENTORY SYSTEM 
weaponList = [
    True, # sword 
    True, # gun
    True, # belt
    False, # kniife
    False  # bomb
]
# each item/value in a list is an elemant
# the location of each element in the list is the INDEX
# first element is index[0]
# shortcut to last element is index[-1]
# weaponNum = 0
# while weaponNum < len(weaponList): 
#     if weaponNum == 0 and weaponList[0] == True:
#         print("Your character is equipped with a sword.\n")
#     if weaponNum == 1 and weaponList[1] == True:
#         print("Your character is equipped with a gun.\n")
#     if weaponNum == 2 and weaponList[2] == True:
#         print("Your character is equipped with a belt.\n")
#     if weaponNum == 3 and weaponList[3] == True:
#         print("Your character is equipped with a knife.\n")
#     if weaponNum == 4 and weaponList[4] == True:
#         print("Your character is equippped with a bomb.\n")
#     weaponNum += 1

# tem Exists in inventory
doorKeys = [
    "red",
    "black",
    "green",
    "pink"
]
item = input("Which key do you require?\n").upper().lower()
if item in doorKeys:
    print(f"You have the {item} key!\n")
else:
    print(f"You do not have the {item} key.")




enemyBase = [
    "Troll",
    "Zombie",
    "Vanpire",
    "Dwarfs",
    "Dragon"
]

enemyType = [
    "Warrior",
    "Wizard",
    "Assassin",
    "Berserker",
    "Paladin"
]

enemyPrefix = [
    "Fire-Breathing",
    "Gargantuan",
    "Invisible",
    "Vampiric",
    "Exploding",
]

mport random

# Index Range (0, 4)
enemyNames = []
while len(enemyNames) < 15:
    enemyBaseGen = enemyBase[random.randint(0,4)]
    enemyTypeGen = enemyType[random.randint(0,4)]
    enemmyPrefixGen = enemyPrefix[random.randint(0,4)]
    newEnemy = enemyPrefixGen + " " + enemyBaseGen + " " + enemyTypeGen
    enemyNames.append(newEnemy)

print(enemynames)