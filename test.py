import random

def roll_dice():
    dice_total = random.randint(1, 3) + random.randint(1, 3)
    return dice_total

player1 = input("Enter player1 Name: ")
player2 = input("Enter player2 Name: ")

roll1 = roll_dice()
roll2 = roll_dice()


print(player1, 'Rolled', roll1)
print(player2, 'Rolled', roll2)

if roll1 > roll2:
    print(player1, "Win!")
elif roll2 > roll1:
    print(player2, "Win!")
else:
    print("You Tie!")



