def calcSum(val):
    return sum(range(1, val + 1))
    
def calcProduct(val):
    prod = 1
    for item in range(1, val + 1):
        prod *= item
    return prod


print('Please enter an integer greater than 0:')
val = int(input())
print('Enter "s" to compute the sum, or "p" to compute the product.')
type_char = input()

valid = True

if type_char == 's':
    type = "Sum"
    result = calcSum(val);
elif type_char == 'p':
    type = "Product"
    result = calcProduct(val)
else:
    valid = False


if valid:
    print(f'The {type} of the integers between 1 and {val} is {result}.')
else:
    print("Please enter only 's' or 'p'")