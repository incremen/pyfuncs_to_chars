constructible = {\
    0: sum(range(sum(range(len(chr(ord(min(str(not()))))))))), # 3 etc.
    1: len(chr(ord(min(str(not()))))),
    4: len(str(not())),                
    6: sum(range(len(str(not())))), 
    84: ord(min(str(not()))),              
    3486: sum(range(ord(min(str(not()))))), 
}

def show_constructible(d=constructible):
    print("Constructible numbers so far:\n")
    for name, expr in d.items():
        try:
            print(f"{name:25s} -> {expr}")
        except Exception as e:
            print(f"{name:25s} -> ERROR ({e})")

if __name__ == "__main__":
    show_constructible()