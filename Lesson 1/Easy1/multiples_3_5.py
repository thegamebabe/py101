def multisum(val):
    num_list = list(range(1, val + 1))
    mutliples_list = [num for num in num_list if (num % 3 == 0 or num % 5 ==0)]
    return sum(mutliples_list)




print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)