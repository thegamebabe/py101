def center_of(sentence):
    temp_list = list(sentence)
    length = len(temp_list)
    center = length // 2;
    if(length % 2 == 0):
        char1 = temp_list[center - 1]
        char2 = temp_list[center]
        return char1 + char2
    else:
        return temp_list[center]
    




print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True