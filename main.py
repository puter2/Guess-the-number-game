import random
import os

def cls() -> None:
    """clear the console"""
    os.system('cls' if os.name=='nt' else 'clear')

def get_target() -> int:
    """choose random number"""
    return random.randint(1, 100)

def choose_difficulty() -> str:
    """ask player for difficulty"""
    while True:
        difficulty = input("Choose difficulty (easy/hard)").lower().strip()
        if difficulty == "easy" or difficulty == "hard":
            return difficulty

play = True
while play:
    res = ''
    diff = choose_difficulty()
    guess = 0
    counter = 0
    target = get_target()
    while True:
        if diff == 'hard':
            cls()
        print(res)
        guess = input("Guess the number: ")
        counter += 1
        if guess.isdigit():
            guess = int(guess)
            if guess < target:
                res = "Too small!"
                # print("Too small!")
            elif guess > target:
                res = "Too big!"
                # print("Too big!")
            else:
                print("You win!")
                print(f"You guessed in {counter} tries, congrats!")
                break
        else:
            print("It's not a number!")

    ans = input("Play again? (y/n): ")
    if ans.lower() == "n":
        play = False