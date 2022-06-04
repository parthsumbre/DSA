'''Write a recursive function
 that takes a number and returns the sum of 
 all the numbers from zero to that number.'''

from tkinter import N


def sumofno(n): # Function
    if n==0: # Base Case
        return n # doesn't return null value
    else:
        return n + sumofno((n-1)) # Recursive function

n = 100
print(sumofno(n)) # order value 