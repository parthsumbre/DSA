'''
A string is entered through the keyboard,  Write a recursive 
function that counts the number of vowels_in_the_string.
'''
'''
Q.8 A string is entered through the keyboard, Write a recursive 
function that check whether the string is a palindrome or not.

Q.9 Write a recursive function that reverse the list of numbers that it receives.

Q.10 A list contains some negative and some positive integers. Write a 
recursive function that sanitizes the list by replacing all negative numbers with 0.
'''
import time



def vowels(strg):
    if strg == "":
        return 0
    elif  strg[0] in ["a","e","i","o","u"]:
        return 1 + vowels(strg[1:])
    else:  
        return 0 + vowels(strg[1:])



start = time.time()
strg ="abcdefghijklmnopqrstuvwxyz"
print(vowels(strg))
end = time.time()
print(end-start)