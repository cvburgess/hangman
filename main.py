# Hangman by Charles Burgess

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
