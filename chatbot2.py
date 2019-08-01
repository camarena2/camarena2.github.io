print ("Hello! I am Chatbot.")

from random import randint


c = ["Rock", "Paper", "Scissors"]


computer = c[randint(0,2)]


answer = False

while answer == False:

    answer = input("Rock, Paper, Scissors?")
    if answer == computer:
        print("Tie!")
    elif answer == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", answer)
        else:
            print("You win!", answer, "smashes", computer)
    elif answer == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", answer)
        else:
            print("You win!", answer, "covers", computer)
    elif answer == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", answer)
        else:
            print("You win!", answer, "cut", computer)
    else:
        print("That's not a valid play. Try again!")

    answer = False
    computer = c[randint(0,2)]
