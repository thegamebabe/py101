
while True:
    amount = float(input("What is the loan amount? "))
    while amount <= 0:
        amount = float(input("Please enter a positive loan amount. "))
    
    apr = 0
    apr = float(input("What is the APR? "))
    while apr <= 1:
        apr = float(input("Must be in the format of 5 rather than .05"))

    monthly_duration = int(input("What is the duration (in months)? "))
    while monthly_duration <= 0:
        monthly_duration = float(input("Please enter a positive \
                                        monthly duration. "))
    
    interest_rate = (apr / 12) / 100
    
    payment = (amount * (interest_rate / (1 - 
                (1 + interest_rate) ** (-monthly_duration))))
    
    print(f"The monthly payment will be ${payment:.2f}")
    try_again = ""
    while True:
        try_again = input("Would you like to calculate another payment (y/n)? ")
        if try_again[0].lower() == 'y' or try_again[0].lower() == 'n':
            break
        print("Please enter 'y' or 'n'")
    if try_again[0].lower() == 'n':
        break


# def prompt(message):
#     print(f"==> {message}")

# def invalid_number(number_str):
#     try:
#         number = float(number_str)
#         if number <= 0:
#             raise ValueError(f"Value must be > 0: {number_str}")
#     except ValueError:
#         return True

#     return False

# prompt("Welcome to Mortgage Calculator!")

# while True:
#     prompt("---------------------------------")

#     prompt("What's the loan amount?")

#     amount = input()
#     while invalid_number(amount):
#         prompt("Must enter a positive number")
#         amount = input()

#     prompt("What is the interest rate?")
#     prompt("(Example: 5 for 5% or 2.5 for 2.5%)")

#     interest_rate = input()

#     while invalid_number(interest_rate):
#         prompt("Must enter a positive number")
#         interest_rate = input()

#     prompt("What is the loan duration (in years)?")
#     years = input()

#     while invalid_number(years):
#         prompt("Must enter a positive number")
#         years = input()

#     annual_interest_rate = float(interest_rate) / 100
#     monthly_interest_rate = annual_interest_rate / 12
#     months = float(years) * 12
#     loan_amount = float(amount)

#     monthly_payment = loan_amount * (
#         monthly_interest_rate /
#             (1 - (1 + monthly_interest_rate) ** (-months))
#     )

#     prompt(f"Your monthly payment is: ${monthly_payment:.2f}")

#     prompt("Another calculation?")
#     answer = input().lower()
#     while True:
#         if answer.startswith('n') or answer.startswith('y'):
#             break

#         prompt('Please enter "y" or "n".')
#         answer = input().lower()

#     if answer[0] == 'n':
#         break