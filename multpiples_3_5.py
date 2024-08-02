#Multiples of 3 and 5

  #Created by Julien Palard
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
