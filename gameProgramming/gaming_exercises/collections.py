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
    False, # gun
    False, # belt
    False, # kniife
    False  # bomb
]
# each item/value in a list is an elemant
# the location of each element in the list is the INDEX
# first element is index[0]
# shortcut to last element is index[-1]
