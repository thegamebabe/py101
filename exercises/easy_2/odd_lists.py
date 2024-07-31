def oddities(vals):
    new_list = list()
    for index in list(range(0, len(vals), 2)):
        new_list.append(vals[index])
    return new_list

# Slicing Technique
# def oddities(lst):
#     return lst[::2]


print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True


