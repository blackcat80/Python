import sys

# Verify the number of arguments
if len(sys.argv) != 3:
    print("Error: two integer arguments are required")
    print("Usage: python3 operations.py 3 19")
    sys.exit()

# Verify that both arguments are integers
try:
    A = int(sys.argv[1])
    B = int(sys.argv[2])
except ValueError:
    print("Error: both arguments must be integers")
    sys.exit()

# Perform the operations
try:
    sum = A + B
    difference = A - B
    product = A * B
    quotient = A / B
    print(f"The sum of {A} and {B} is {sum}")
    print(f"The difference of {A} and {B} is {difference}")
    print(f"The product of {A} and {B} is {product}")
    print(f"The quotient of {A} and {B} is {quotient}")
except ZeroDivisionError:
    print("Error: division by zero is not possible")