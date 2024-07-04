#Here's a simple dice roller program in Python:

import random

def roll_dice(sides=6):
    return random.randint(1, sides)

print("Dice Roller")  
print("------------")

while True:
    num_dice = int(input("Enter number of dice to roll (1-6): "))
    if num_dice < 1 or num_dice > 6:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    sides = int(input("Enter number of sides on each die (4, 6, 8, 12, 20): "))
    if sides not in [4, 6, 8, 12, 20]:
        print("Invalid input. Please enter a valid number of sides (4, 6, 8, 12, 20).")
        continue

    results = [roll_dice(sides) for _ in range(num_dice)]
    print(f"You rolled: {results}")
    print(f"Total: {sum(results)}")

    repeat = input("Roll again? (y/n): ")
    if repeat.lower() != "y":
        break

# This program allows you to roll a specified number of dice with a specified number of sides. The results are displayed, along with the total sum.

# Example output:

# Dice Roller
# ------------
# Enter number of dice to roll (1-6): 3
# Enter number of sides on each die (4, 6, 8, 12, 20): 6
# You rolled: [4, 3, 6]
# Total: 13
# Roll again? (y/n): y
# Enter number of dice to roll (1-6): 2
# Enter number of sides on each die (4, 6, 8, 12, 20): 20
# You rolled: [14, 7]
# Total: 21
# Roll again? (y/n): n

# Have fun rolling dice!
