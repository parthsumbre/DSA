''' Least Common Multiple(LCM) of 2 Numbers'''
'''Greatest Common Divisor(GCD) of 2 Numbers'''

def gcd(num1, num2):
    if num1 == 0:
        return num2
    return gcd(num2%num1 , num1)#15 24
 
def lcm(num1,num2):
    return (num1 / gcd(num1,num2)*num2)


num1,num2 = 300,500

a = (gcd(num1,num2))
b = (lcm(num1,num2))

print("GCD ", a )# 15 x 20 = 60 * 5 = 300
print("LCM ", b )
print(num1*num2)
print(a*b)
    