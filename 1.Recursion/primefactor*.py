

'''If a positive integer is entered 
through the keyboard, write a recursive 
function to obtain the prime factors of the number. '''


def factor(i,f):
    if i < f:
        return []
    if i % f == 0:
        '''300, 2
                    #150, 2
                    #75, 2
                #75, 3
                    #25, 3
                #25, 4
                #25, 5
                    #5, 5
                #1, 5   ''' 
        return [f] + factor (i / f, 2)
    return factor (i, f + 1)
    

   


print(factor(1503,2))