from random import randint


c = ["Rock", "Paper", "Scissors"]


computer = c[randint(0,2)]

answer = False

while answer == False:

    print("Hi my name is Chatbot! Lets play a game. What do you choose?")
    answer = input("Rock, Paper, Scissors.")

    if answer == computer:
        print("Tie!")
    if answer == "Rock":
            say_rock()
    elif answer == "Paper":
                say_paper()
    elif answer == "Scissors":
                    say_scissors()

def say_rock():
    if computer == "Paper":
            print("You lose!", computer, "covers", answer)
    else:
        print("You win!", answer, "smashes", computer)

def say_paper():
    if computer == "Scissors":
            print("You lose!", computer, "cut", answer)
    else:
        print("You win!", answer, "covers", computer)

def say_scissors():
    if computer == "Rock":
            print("You lose...", computer, "smashes", answer)
    else:
        print("You win!", answer, "cut", computer)
