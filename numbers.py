#a sample of numerical challenges 
  #note: all changes Created by Julien Palard, unless otherwise specified

import math 

#Multiples of 3 and 5
  #Write a program that finds the sum of all natural numbers below 1000 (< 1000) that are multiples of 3 or 5, and prints it.
  #If we list all the natural numbers below 20 (<20) that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, 18. The sum of these multiples is 78.
  #Note that 15 is only counted once.

sum = 0;
multiplier = 1;

while multiplier <= 333:
    three_mult = 3 * multiplier
    sum += three_mult
    if multiplier < 200:
        five_mult = 5 * multiplier
        if five_mult % 3 > 0:
            sum += five_mult
    multiplier += 1;

print(sum)

#Check if a number is prime
  #Define the function is_prime(n).
  #n is number that the function is_prime takes as a parameter.
  #The function is_prime return True if n is a prime number, False otherwise.

def is_prime(n):
    check = 2;
    if n < check:
        return False
    max_check = int(math.sqrt(n)) + 1
    while check < max_check:
        if n % check == 0:
            return False
        check += 1
    return True

#Next prime
  #Provide a script that computes, then prints the first prime number greater than 100_000_000

n = 100000001
cork = True

while cork:
    if is_prime(n):
        print(n);
        cork = False;
    n += 1;

#Print every prime number in a range
  #Provide a script that print every prime number in the range [10000;10050], on one line, separated by comas and spaces.

def is_prime(n):
    check = 2;
    if n < check:
        return False
    max_check = int(math.sqrt(n)) + 1
    while check < max_check:
        if n % check == 0:
            return False
        check += 1
    return True

primes = [str(x) for x in range(10000,10051) if is_prime(x)]
delim = ", "
print(delim.join(primes))

#Friday the 13th
  #Find the next friday the 13th.
  #Write a function named friday_the_13th, which takes no parameter, and just returns the date of the next friday the 13th.
  #If today is a friday the 13th, return it, not the next one. Return the date as a string of the following format: YYYY-MM-DD.

from datetime import datetime, timedelta

def friday_the_13th():
    now = datetime.now() 
    wday = now.weekday()
    day_diff = 4 + 7 - wday
    day_diff = day_diff if day_diff < 7 else day_diff - 7
    friday = now + timedelta(days=day_diff)
    is_13 = friday.day == 13
    
    while is_13 == False:
        friday = friday + timedelta(days=7)
        is_13 = friday.day == 13
    
    return friday.strftime("%Y-%m-%d")

