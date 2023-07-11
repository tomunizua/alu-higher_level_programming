#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if argv[2] == "+":
        result = add(int(argv[1]), int(argv[3]))
    elif argv[2] == "-":
        result = sub(int(argv[1]), int(argv[3]))
    elif argv[2] == "*":
        result = mul(int(argv[1]), int(argv[3]))
    else:
        result = div(int(argv[1]), int(argv[3]))
    print(f"{int(argv[1])} {argv[2]} {int(argv[3])} = {result}")
