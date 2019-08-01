

print(" Welcome to the Secret Word Game. Guess a letter in the word, then press enter:")

from random import choice

word = choice(["table", "chair", "bottle", "plate", "parade", "coding", "teacher", "markers", "phone", "grill", "friends", "fourth", "party"])

guessed = []

while True:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        print("Congrats! You guessed correctly:", word)
        break

    print("Guess a letter:", out)
    guess = input()

    if guess in guessed:
        print("You already guessed this letter! Try again!")
    elif guess in word:
        print("Yay! Good Job!")
        guessed.append(guess)
    else:
        print("Try Again!")

    print()
