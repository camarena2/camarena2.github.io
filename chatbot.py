# --- Put your main program below! ---
def intro():
    print("Hi my name is Chatbot!")


def process_input(answer):
  if answer == "Rock":
    say_rock()
  elif answer == "Paper":
    say_paper()
  elif answer == "Scissors":
      say_scissors()

def say_rock():
  print("Tie!")

def say_paper():
  print("You Won! Paper covers rock.")

def say_scissors():
  print("You lost! Rock smashes Scissors. ")

def main():
  intro()
  while True:
    answer = input("Lets play a game. Rock, Paper, Scissors. What do you choose?")
    process_input(answer)

if __name__ == "__main__":
  main()
