'''Q.9 Write a recursive function that reverse_the_list_of_numbers that it receives.'''

def reverseList(lst):
    if len(lst) ==  0:
        return []
    else:
        return [lst[-1]] + reverseList(lst[:-1])

lst = [10,20,30,40,50,60,70,80,90,100]
print(reverseList(lst))