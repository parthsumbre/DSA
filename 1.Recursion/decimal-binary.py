def decimal_binary(num):
    if num == 0:
        return num
    else:
        r = num%2 
        print(r, end='')
        decimal_binary(num//2)

num= 10

decimal_binary(num)
