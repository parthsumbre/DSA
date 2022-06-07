'''
A string is entered through the keyboard,  Write a recursive 
function that counts the number of vowels_in_the_string.
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




# 0, 1, 1, 2, 3, 5, 8, 13, 21, n 