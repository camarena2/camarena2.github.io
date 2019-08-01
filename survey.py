import json

def main():
  data_list = []

  again = True
  while again == True:
    name = input("What's your name? ")
    age = input("How old are you? ")
    siblings = input("How many siblings do you have? ")
    brand = input("What is your favorite brand? ")
    color = input("What is your favorite color? ")

    answers = {"Name":name, "Age":age, "Siblings":siblings, "Brand":brand, "Color":color}

    data_list.append(answers)

    answer = True
    while answer == True:
        collect = input("New Survey? yes or no: ")
        if collect == "yes":
            again = True
            answer = False
        elif collect == "no":
            print(data_list)
            again = False
            answer = False

    with open("survey.json", "w") as json_file
        json.dump(data_list, json_file)

if __name__ == "__main__":
    main()
