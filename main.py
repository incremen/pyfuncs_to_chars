constructible = {
    0: (lambda: sum(range(sum(range(len(chr(ord(min(str(not()))))))))), "sum(range(sum(range(len(chr(ord(min(str(not())))))))))"),
    1: (lambda: len(chr(ord(min(str(not()))))), "len(chr(ord(min(str(not())))))"),
    4: (lambda: len(str(not())), "len(str(not()))"),
    6: (lambda: sum(range(len(str(not())))), "sum(range(len(str(not()))))"),
    84: (lambda: ord(min(str(not()))), "ord(min(str(not())))"),
    3486: (lambda: sum(range(ord(min(str(not()))))), "sum(range(ord(min(str(not())))))"),
}

def show_constructible(d=constructible):
    print("Constructible numbers so far:\n")
    for value, (func, expr_str) in d.items():
        try:
            expr_val = func()
            print(f"{expr_val} = {expr_str}")
        except Exception as e:
            print(f"{value:6} -> ERROR ({e}) | {expr_str}")

if __name__ == "__main__":
    show_constructible()