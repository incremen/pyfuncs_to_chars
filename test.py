# Dictionary to store constructible numbers and their expressions
constructible = {}

# Add a big number as an example (using 84, which is constructible)
constructible[84] = (lambda: ord(min(str(not()))), 'ord(min(str(not())))')

def build_number(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        # next(reversed(range(N))) returns N-1
        return f"next(reversed(range({n+1})))"

# Recursively build every number less than 100
for i in range(100):
    constructible[i] = (lambda n=i: eval(build_number(n)), build_number(i))

# Print the dictionary
for k in sorted(constructible):
    func, expr = constructible[k]
    try:
        val = func()
        print(f"{k}: {val} = {expr}")
    except Exception as e:
        print(f"{k}: ERROR ({e}) | {expr}")
