#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    a = int(sys.argv[1])
    op = int(sys.argv[2])
    b = int(sys.argv[3])
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for op in range("+", "-", "*", "/"):
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        
