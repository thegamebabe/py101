CONVERSION = 10.7639 

print("Enter the length of the room")
length = float(input())

print("Enter the width of the room")
width = float(input())

print(f'The area of the room is {length * width:.2f} meters and {length * width * CONVERSION:.2f} feet')