'''
write a recursive function to obtain average of all numbers present in the given list
'''

def listavg(lst,n):  
    if len(lst) == 1:
        return lst[0]/n
    else:
        return (lst[len(lst)-1]/n) + listavg(lst[:len(lst)-1], n)


lst = [1,2,3,4,5]
n = len(lst)
print(listavg(lst, n))