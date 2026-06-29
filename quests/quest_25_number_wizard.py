secret = 42
guess = int(input("Guess the number: "))
while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))
print("You got it!")
