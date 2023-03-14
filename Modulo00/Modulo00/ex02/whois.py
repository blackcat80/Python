import sys

if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
        if num == 0:
            print("The number is zero.")
        elif num % 2 == 0:
            print("The number is pair.")
        else:
            print("The number is odd.")
    except ValueError:
        print("Error: Argument is not an integer.")
else:
    print("Error: the entered value is not an integer.")

# Otra opcion sin usar gestion de errores

'''
if len(sys.argv) != 2:
    print("Error: Please provide one integer argument.")
else:
    num = sys.argv[1]
    if not num.isdigit():
        print("Error: Argument is not an integer.")
    else:
        num = int(num)
        if num == 0:
            print("The number is zero.")
        elif num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
'''