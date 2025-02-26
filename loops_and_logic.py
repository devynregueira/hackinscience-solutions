#a series of challenges emphasizing logic and iteration

#Reverse Roman Numerals
  #Created by Julien Palard
  #Write a function named from_roman_numeral that return the value of a given roman numeral.

convert = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def from_roman_numeral(r_n):
    counter = 0;
    digits = [convert[r_n[x]] for x in range(0,len(r_n))]
    patches = [];
    
    for ind, x in enumerate(digits):
        prv = ind - 1
        is_new_patch = True if ind == 0 else True if digits[prv] != x else False
        
        if is_new_patch:
            patches.append([x])
        else:
            patches[-1].append(x)

    for ind, patch in enumerate(patches):
        degree = patch[0]
        count = len(patch)
        charge = ind == len(patches) - 1
        charge = 1 if charge else -1 if degree < patches[ind + 1][0] else 1
        
        counter += degree * count * charge
    
    return counter


#Sets of love
  #Created by Antoine Mazières
  #Once upon a time, in Paris, the city of romance, Bob and Alice met and fall in love with each other.
  #Exercise 1: To fullfill their romance, they want to meet as much as possible. They share their daily paths among Paris districts to know where they can find each other at the same place.
    #As you know there is 20 districts in Paris: (set of districts is provided)
    #Code a function named love_meet taking bob and alice's daily paths as two lists and returning a set of the districts they both visit during the day.
  #Exercise 2: Alice is bored and get a crush for the strong and handsome Silvester. In order to have an affair with Silvester she must find out where both Silvester and her go during the day. But to avoid an unfortunate encounter with Bob, she must be sure Bob doesn't go there also.
    #For the sake of her new love, provide Alice the function affair_meet that takes Bob, Alice and Silvester daily path in Paris, and returns a set of all places where Alice and Silvester can meet and be sure Bob won't be.

def love_meet(bob, alice):
    intercepts = [x for x in bob if x in alice]
    return set(intercepts)

def affair_meet(bob, alice, silvester):
    forays = [x for x in alice if x in silvester and x not in bob]
    return set(forays)


#Sort students
  #Created by Antoine Mazières
  #In this exercise we represent students as a pair of (mark, full_name), so a tuple of two elements.
  #And in this exercises we represent students as lists of pairs, like: students = [(85, "Susan"), (6, "Joshua"), (37, "Jeanette")]
  #Part 1: 
    #Write a function named sort_by_mark that take as argument a list of students and returns a copy of it sorted by mark in descending order
  #Part 2: 
    #Write a function named sort_by_name that take as argument a list of students and returns a copy of it sorted by name in ascending order

def sort_by_mark(my_class):
    return sorted(my_class,key=lambda x: x[0],reverse=True)

def sort_by_name(my_class):
    return sorted(my_class,key=lambda x: x[1],reverse=False)


#The missing card
  #Created by Julien Palard
  #Write a function named missing_card that given a card game returns the (single) missing card name.
  #The card game will be given as a single string of space-separated cards names. You'll always be given 51 cards, and you have to return the missing one.
  #A card is represented by its color and value, the color being in {"S", "H", "D", "C"} and the value being in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}, for a total of 52 possibilities.

def missing_card(cards):
    clrs = ["S","H","D","C"]
    vals = [x for x in range(2,11)]
    vals = vals + ["J","Q","K","A"]
    vals = [clr + str(val) for val in vals for clr in clrs]
    splt = cards.split()
    
    return [x for x in vals if x not in splt][0]


#Perfect deck shuffle
  #Created by Julien Palard
  #Simulate a perfect suffle of a deck of cards. 
  #A perfect shuffle of a deck of card is splitting a deck of cards into equal halves, and perfectly interleaving them. Perfectly shuffling [1, 2, 3, 4, 5, 6] gives [1, 4, 2, 5, 3, 6].
  #You'll expose a perfect_shuffle(deck) function, perfectly shuffling the given iterable.

def perfect_shuffle(deck):
    half = int(len(deck)/2)
    left = deck[0:half]
    right = deck[half:len(deck)]
    shuffled = [item for pair in zip(left, right) for item in pair]
    return shuffled
