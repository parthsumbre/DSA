'''Python program to find the power of a number using recursion
Given a number N and power P. The task is to write a Python program to 
find the power of a number using recursion.'''

def powerOfNumbers(N,P):
    if P == 1: 
        return N
    return N * powerOfNumbers(N,(P-1))

print(powerOfNumbers(2,4))