'''It is used to find the sum of digits of a number using recursion.'''

def sumofdigit(p):  
    if len(p) == 1:
        return int(p)
    else:
        return int(p[len(p)-1]) + sumofdigit(p[:len(p)-1])
    
p = "148"
print(sumofdigit(p))

