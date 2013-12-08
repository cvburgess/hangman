# Hangman by Charles Burgess

import random

"""

*docs to go here*

"""

welcome_message = """\n
    Hello and welcome to Hangman!\n
    This code was built by Charles Burgess with Python 3.\n
    If you are using Python 2.x you need to wrap all responses
    in quotation marks (\"\") or errors will fly!.\n"""

print(welcome_message)

# Words and Categories

foods = ["apple", "banana", "chocolate", "doughnut", "edamame", "gelato",
         "hamburger", "icing", "jello", "mushroom", "papaya", "quiche",
         "raspberry", "steak", "tangerine", "watermelon", "yams"]

animals = ["ant", "bear", "cougar", "elephant", "flamingo", "gorilla",
           "hedgehog", "kangaroo", "leopard", "mongoose", "narwhal",
           "octopus", "platapus", "ringtail", "snake", "tyrannosaurus",
           "walarus", "yeti", "zebra"]

cities = ["atlanta", "baltimore", "chicago", "denver", "houston",
          "minneapolis", "sacramento", "tampa", "vegas"]

categories = {"animals": animals, "foods": foods, "cities": cities}


def get_category():
    while True:
        category = input("Please pick a category to begin:\n{}\n\n".format(
            '\n'.join(['- {}'.format(c.title()) for c in categories.keys()])))

        if category.lower() in categories.keys():
            return categories[category.lower()]
            break
        else:
            print ("Sorry, \"{}\" is not a valid category. "
                   "Please try again.\n".format(category))
            continue

category = get_category()
word = category[random.randrange(0, len(category))]

print ("Get ready to play! Your word is {}.".format(
    ' '.join(["_" for char in word])))
