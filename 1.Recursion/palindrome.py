'''A string is entered through the keyboard, Write a recursive 
function that check whether the string is a palindrome or not.'''

def palindrome(strg):
    if len(strg) == 1:
        return True
    else:
        if strg[0]==strg[-1]:
            return palindrome(strg[1:-1])
        else:
            return False

strg = input("Enter a String : ")
if palindrome(strg):
    print(strg)
    print("String is palindrome")
else:
    print("String is not palindrome")
