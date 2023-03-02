import sys

## EXCEPTION HANDLING ##

##### handle exception when input is not a number ###
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError: 
    print("Error: Invalid input.")
    sys.exit(1)

##### handle exception when divided by 0 ######
# print out the message and simply exit the program 
# avoid crashing
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")

