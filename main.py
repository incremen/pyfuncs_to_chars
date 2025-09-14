constructible = {
    0: (lambda: sum(range(sum(range(len(chr(ord(min(str(not()))))))))), "sum(range(sum(range(len(chr(ord(min(str(not())))))))))"),
    1: (lambda: len(chr(ord(min(str(not()))))), "len(chr(ord(min(str(not())))))"),
    4: (lambda: len(str(not())), "len(str(not()))"),
    6: (lambda: sum(range(len(str(not())))), "sum(range(len(str(not()))))"),
    84: (lambda: ord(min(str(not()))), "ord(min(str(not())))"),
    3486: (lambda: sum(range(ord(min(str(not()))))), "sum(range(ord(min(str(not())))))"),
}

extra_constructible = {
    'int(not(not()))': (lambda: int(not(not())), 'int(not(not()))'),
    'int(not())': (lambda: int(not()), 'int(not())'),
    'len(str(ord(min(str(not())))))': (lambda: len(str(ord(min(str(not()))))), 'len(str(ord(min(str(not())))))'),
    'len(bin(int(not())))': (lambda: len(bin(int(not()))), 'len(bin(int(not())))'),
    'len(str(not()))': (lambda: len(str(not())), 'len(str(not())))'),
    'len(bin(len(str(not()))))': (lambda: len(bin(len(str(not())))), 'len(bin(len(str(not()))))'),
    'sum(range(len(str(not()))))': (lambda: sum(range(len(str(not())))), 'sum(range(len(str(not()))))'),
}

def show_constructible(d=constructible):
    print("Constructible numbers so far:\n")
    for value, (func, expr_str) in d.items():
        try:
            expr_val = func()
            print(f"{expr_val} = {expr_str}")
        except Exception as e:
            print(f"{value:6} -> ERROR ({e}) | {expr_str}")

def show_extra_constructible(d=extra_constructible):
    print("Extra constructible numbers:\n")
    for name, (func, expr_str) in d.items():
        try:
            expr_val = func()
            print(f"{expr_val} = {expr_str}")
        except Exception as e:
            print(f"{name:25s} -> ERROR ({e}) | {expr_str}")

if __name__ == "__main__":
    show_constructible()
    show_extra_constructible()