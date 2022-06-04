'''We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .'''

def sumofdigit(p):  
    if len(p) == 1:
        return int(p)
    else:
        return int(p[len(p)-1]) + sumofdigit(p[:len(p)-1])
    
n = "148" 
k = 3
p = "12"
print(sumofdigit(p))

