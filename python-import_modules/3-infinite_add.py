#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    final_sum = 0
    for num in (sys.argv[1:]):
        final_sum += int(num)
    print(final_sum)
