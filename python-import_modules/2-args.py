#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_args = len(sys.argv)
    if no_args != 2:
        string = "arguments"
    else:
        string = "argument"
    print(f"{no_args - 1} {string}{'.' if no_args == 1 else ':'}")
    for num in range(1, no_args):
        print(f"{num}: {sys.argv[num]}")
