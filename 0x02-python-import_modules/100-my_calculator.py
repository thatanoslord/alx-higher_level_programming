#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operations = {"+": calc.add, "-": calc.sub, "*": calc.mul, "/": calc.div}

    if operator not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {} {:d} = {:d}".format(
        a, operator, b, operations[operator](a, b)))
