def negative(num):
    if(num > 0):
        # return -abs(number)
        return 0 - num
    else:
        return num
    

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True