#various challenges involving strings

import string

#Print every two letters pair
  #Created by Julien Palard
  #Provide a script printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically.

list = string.ascii_lowercase;
[print(let1 + let2) for let1 in list for let2 in list]

#Print every pair of distinct letters
  #Created by Julien Palard
  #Provide a script printing every possible pairs of two different letters.
  #Only lower case, one pair per line, ordered alphabetically.
  #Don't print pairs consisting of twice the same letter, such as 'aa', 'bb', etc...

list = string.ascii_lowercase;
[print(let1 + let2) for let1 in list for let2 in list if let2 != let1]

#Print sorbet flavors
  #Created by Julien Palard
  #Provide a script printing every possible sorbet duos from a given list of flavors.
  #Don't print recipes with twice the same flavor (no "Chocolate Chocolate"), and don't print twice the same recipe...
  #The flavors are: (flavors are listed); Print one duo per line, and separate flavors by comas

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

while len(FLAVORS) > 1:
    base = FLAVORS.pop(0)
    for flav in FLAVORS:
        print(base + ", " + flav)











