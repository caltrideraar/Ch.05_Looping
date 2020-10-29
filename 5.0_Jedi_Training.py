  #Sign your name: Aaron Caltrider_

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
      x = int(input("Enter a number: "))
      total += x
print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(25):
    print((i+1) * 2)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

var = 11
while var >=1:
   var = var-1
   print (var)
print ("Blast Off!")




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

import random

my_number = random.randrange(50)
print(my_number)

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
zero = 0
neg = 0
pos = 0
total = 0
for i in range(7):
      x = int(input("Enter a number: "))
      total += x
if x > 0:
    pos = pos + 1
else:
    neg = neg + 1
print("The total is:", total)
print("You have", pos, "positive(s).")
print("You have", neg, "negative(s).")
print("You have", zero, "zero(es).")