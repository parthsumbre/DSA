'''A list contains some negative and some positive numbers. 
Write a recursive function that sanitizes the list by replacing all the negative numbers 
with 0.'''

def replaveneg(lst):
    if len(lst) == 1:
        if lst[0] < 0:
            return [0]
        return lst
    
    else:
        if lst[0] < 0:
            lst[0] = 0
            replaveneg[1:]
        else:
            