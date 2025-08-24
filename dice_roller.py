import random 

def roll_dice():
    return random.randint(1,6)

print("Dice Roller Game")
while True:
    input("Press Enter to roll the dice")
    result = roll_dice()
    print(f"You rolled a {result}!")

    if result == 6:
        print("You rolled a 6! Roll again")
        continue
    else:
        print("Next person chance")
        break
