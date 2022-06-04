'''Write a recursive function that takes a string and reverse the string.'''

def reverse_string(str):
    if len(str) == 1:
        return str
    else:
        return str[len(str)-1] + reverse_string(str[:len(str)-1])

str = "sushilkumar"
print(reverse_string(str))
