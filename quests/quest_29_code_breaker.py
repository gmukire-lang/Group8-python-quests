secret_code = 42
attempts = 0

while attempts < 3:
    guess = int(input("Enter the secret code: "))
    attempts += 1
    if guess == secret_code:
        print("Correct! Access granted.")
        break
    else:
        remaining = 3 - attempts
        if remaining > 0:
            print(f"Wrong code. {remaining} attempt(s) remaining.")
        else:
            print("Too many failed attempts. Access denied.")
