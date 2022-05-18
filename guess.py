
import random


class Guess:
    range = 0

    # constructor class set the range
    def __init__(self, range):
        self.range = range

    # the user guess the number
    def user_guess(self):
        random_number = random.randint(1, self.range)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between 1 and {self.range}: "))

            if guess > random_number:
                print("Guess again. Too high.")
            elif guess < random_number:
                print("Guess again. Too low")
        else:
            print("You got it")

    # the computer guess the number
    def computer_guess(self):
        low = 1
        high = self.range
        feedback = ""

        while feedback != "c":
            if low != high:
                guess = random.randint(low, high)  # trows error when equal
            else:
                guess = low  # low == high

            feedback = input(
                f"Is {guess} to low (L), to high (H) or correct (C)...?").lower()
            if feedback == "l":
                low = guess + 1
            elif feedback == "h":
                high = guess - 1
        else:
            print(
                f"Awesome!! The computer guessed your number, \"{guess}\" is correct.")
