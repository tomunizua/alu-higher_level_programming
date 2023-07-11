#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc_f
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calc_f.add(a, b)))
    print("{} - {} = {}".format(a, b, calc_f.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc_f.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc_f.div(a, b)))
