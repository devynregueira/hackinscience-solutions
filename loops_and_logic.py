#a series of challenges emphasizing logic and iteration

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

