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
    False, # sword 
    True, # gun
    True, # belt
    False, # kniife
    False  # bomb
]
# each item/value in a list is an elemant
# the location of each element in the list is the INDEX
# first element is index[0]
# shortcut to last element is index[-1]
weaponNum = 0
while weaponNum < len(weaponList): 
    if weaponList[0] == True:
        print("Your character is equipped with a sword.\n")
    if weaponList[1] == True:
        print("Your character is equipped with a gun.\n")
    if weaponList[2] == True:
        print("Your character is equipped with a belt.\n")
    if weaponList[3] == True:
        print("Your character is equipped with a knife.\n")
    if weaponList[4] == True:
        print("Your character is equippped with a bomb.\n")
    weaponNum += 1