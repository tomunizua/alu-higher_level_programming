#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    attributes = dir(hidden_4)
    for names in attributes:
        if names[0] != "_" or names[1] != "_":
            print(names)
