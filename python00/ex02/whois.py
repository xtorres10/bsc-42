import sys

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print("Error")
else:
    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    elif number % 2:
        print("I'm Odd")
    else:
        print("I'm Even")