secret_key = 7

while True:
    guess = int(input("geuss the secret key: "))

    if guess == secret_key:
        print("You guessed it right!")
        break

    print("Wrong guess. Try again.")