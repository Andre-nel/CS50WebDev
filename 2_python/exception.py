import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit(1)

try:
    result = x / y
    print(f"{x} / {y} = {result}")
except ZeroDivisionError:
    print(f"Error: You cannot divide by {y}!")
    sys.exit(1)
