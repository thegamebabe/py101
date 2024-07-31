num1 = float(input("Enter number one: "))

num2 = float(input("Enter number two: "))

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Product: {num1} * {num2} = {num1 * num2}")
print(f"Quotient: {num1} / {num2} = {num1 / num2}")
print(f"Floor Quotient: {num1} // {num2} = {num1 // num2}")
print(f"Remainder: {num1} % {num2} = {num1 % num2}")
print(f"Power: {num1} ** {num2} = {num1 ** num2}")



# def calculate(first, second, operator):
#     match operator:
#         case '+':  return first + second
#         case '-':  return first - second
#         case '*':  return first * second
#         case '/':  return first / second
#         case '//': return first // second
#         case '%':  return first % second
#         case '**': return first ** second

# first_float = float(input("==> Enter the first number:\n"))
# second_float = float(input("==> Enter the second number:\n"))
# for operator in ['+', '-', '*', '/', '//', '%', '**']:
#     operation = f"{first_float} {operator} {second_float}"
#     result = calculate(first_float, second_float, operator)
#     print(f"==> {operation} = {result}")