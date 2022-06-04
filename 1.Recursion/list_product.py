'''
Write a recursive function that takes a list of numbers as an input and 
returns the product of all the numbers in the list.
'''

def list_product(lst): # function
    if len(lst) == 1: # base case
        return lst[0] 
    else:
        return lst[len(lst)-1] * list_product(lst[:len(lst)-1]) # Recursive

lst = [1,2,3,4,5,6]
print(list_product(lst))