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
            lst[0]=0
            return [lst[0]] + replaveneg(lst[1:])
        else:
            return [lst[0]] + replaveneg(lst[1:])
            
lst = [-1,1,-2,2]
print(replaveneg(lst))

