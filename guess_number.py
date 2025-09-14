from random import randint
from logo import logo_game
print(logo_game)

computer_number = randint(1, 100)
attempts = 10

print(f"You have {attempts} attempts to guess the computer's number!")

while attempts > 0:
    try: player_number = int(input(f"Guess a number between 1 and 100:\n"))
    except ValueError: print("🔥Invalid input, please try again.🔥"); continue
    attempts -= 1
    if player_number == computer_number:
        print("You won!🥳")
        break
    elif player_number < computer_number: print(f"Too low!👇\nAttempts left: {attempts} attempts remaining.")
    else: print(f"Too high!☝️\nAttempts left:{attempts} attempts remaining.")
else: print("😭😭😭You loose!😭😭😭")
