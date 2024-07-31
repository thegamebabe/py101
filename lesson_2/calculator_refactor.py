def prompt(msg):
    print(f'{msg}')

def is_not_valid_num(num_string):
    try:
        int(num_string)
    except ValueError:
        return True
    return False

def is_not_valid_operation(num_string):
    if is_not_valid_num(num_string):
        return True
    if int(num_string) not in [1, 2, 3, 4]:
        return True
    return False


print('Welcome to my calculator!')

prompt("What's the first number?")
number1 = input()
while is_not_valid_num(number1):
    print("Not a valid number")
    number1 = input()
number1 = int(number1)

prompt("What's the second number?")
number2 = input()
while is_not_valid_num(number2):
    print("Not a valid number")
    number2 = input()
number2 = int(number2)

print("""What operation would you like to perform?
1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()

while is_not_valid_operation(operation):
    print("Please select a valid option")
    operation = input()
operation = int(operation)

if operation == 1:
    output = number1 + number2
elif operation == 2:
    output = number1 - number2
elif operation == 3:
    output = number1 * number2
elif operation == 4:
    output = number1 / number2

# # match operation:
#     # case 1:
#     #     output = number1 + number2
#     # case 2:
#     #     output = number1 - number2
#     # case 3:
#     #     output = number1 * number2
#     # case 4:
#     #     output = number1 / number2

print(f"The result is: {output}") # pylint: disable=E0606