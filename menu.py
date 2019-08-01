import random
appetizer = ("garlic bread", "salad", "soup", "calamari")
main = ("pasta", "chicken", "quesadillas", "tacos", "sandwich", "caesar salad", "pizza")
dessert = ("cheesecake", "tiramisu", "canoli", "strawberry shortcake", "ice cream", "lemon bars")
first = random.choice(appetizer)
second = random.choice(main)
third = random.choice(dessert)
menu = (first + " " + second + " " + third + " "
)
print("Your menu is: " + menu)
