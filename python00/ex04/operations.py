import sys

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    sum = a + b
    rest = a - b
    prod = a * b
    if b == 0:
        quot = "Error (division by zero)"
        porc = "Error (modulo by zero)"
    else:
        quot = a / b
        porc = a % b
    print(f'Sum:\t\t{sum}\nDifference:\t{rest} \
    \nProduct:\t{prod}\nQuotient:\t{quot}\nRemainder:\t{porc}')

if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>\
            \nExample:\n\tpython operations.py 10 3")
elif len(sys.argv) != 3:
    print("Error, expect 2 numers")
elif not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    print("Error, expect int numbers")
else:
    main()