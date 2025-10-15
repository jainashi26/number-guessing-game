import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

n = random.randint(1, 100)
guesses = 0
a = None

while a != n:
    try:
        a = int(input("👉 Guess the number: "))
        guesses += 1

        if a > n:
            print("📉 Lower number please!\n")
        elif a < n:
            print("📈 Higher number please!\n")
        else:
            print(f"🎉 You guessed it right! The number was {n}.")
            print(f"✅ You guessed it in {guesses} attempts!")
    except ValueError:
        print("⚠️ Please enter a valid integer.\n")
