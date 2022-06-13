# def fun(x,y):
#     if x==0:
#         return y
#     else:
#         return fun(x-1, x*y)
#         #4 2 
#         #3 8
#         #2 24
#         #1 48
#         #0 48 -> 48

# print(fun(4,2))

def fun(num):
    if num>100:
        return num-10
    else:
        print(num)
        return fun(fun(num+11))
    #99 
        #110
    #100
        #111
    #101 
        #91
    #102
        #92
    #103
        #93
    #104
        #94
        #95
        #96
        #97
        #98
        #99
    #110
        #100
    #111
        #101
    #91      
           
    
        
print(fun(75))