import random

secret_number = random.randint(1, 99)
tries = 0
print(f"This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
while True:
    entry = input(f"What's your guess between 1 and 99?\n")
    if entry == "exit":
        print("¡Goodbye!")
        break
    elif entry == secret_number & tries == 1:
        print(f"¡Congratulations! You got it on your first try!\n")
    elif secret_number == 42:
        print(f"The answer to the ultimate question of life, the universe and everything is 42.")
    
    tries += 1
    try:
        entry = int(entry)
    except ValueError:
        print("Introduce a valid number!")
        continue
    
    if entry == secret_number:
        print(f"\n¡Well Done! you won in {tries} attempts.\n")
        break
    elif entry < secret_number:
        print("Too low.\n")
    else:
        print("Too high.\n")
