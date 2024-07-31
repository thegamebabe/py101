def xor(val1, val2):
    if(val1 and not val2):
        return True
    elif(not val1 and val2):
        return True
    else:
        return False
# return bool((value1 and not value2) or (value2 and not value1))    


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)