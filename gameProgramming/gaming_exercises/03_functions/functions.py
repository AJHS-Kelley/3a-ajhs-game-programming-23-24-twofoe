
































def rolldice(numRoll, sizeRoll):
    count = 0 
    sum = 0
    while count < numRolll:
        roll = random.randint(1, sizeRoll)
        #print(f"Roll #{count}: {roll}\n")
        sum += roll 
        count += 1
    #print(sum)
    return sum

# print("D4 Rolls")
# d4Sum = rollDice(10, 4)
# print("D20 Rolls")
# d20Sum = rollDice(2, 20)

# print(d4Sum)
# print(d20Sum)