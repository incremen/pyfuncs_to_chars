import sys
from anchors import build_char

if __name__ == '__main__':
    while True:
        char = input("Enter a character: ")
        if len(char) != 1:
            print("Please enter exactly one character.")

        expr = build_char(char)
        print(f"\nExpression for '{char}' (code point {ord(char)}):")
        print(expr)
        print(f"\nVerify: eval gives '{eval(expr)}'")

