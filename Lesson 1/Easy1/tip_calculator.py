print("What is the bill?")
bill = float(input())

print("What is the tip percentage?")
tip_percent = float(input())

tip = bill * tip_percent / 100
bill = bill + tip

print(f'The tip is ${tip:.2f}')
print(f'The total is ${bill:.2f}')

