ai wrote this readme for now sorry i couldnt be bothered

# pyfuncs_to_chars

Write any character as a Python expression using **only builtin function calls** — no numeric literals, no string literals, no operators.
Each function must take in only one argument - pow(a,b) isn't allowed

## How it works

Everything starts from one trick:

```
not()  →  True
str(not())  →  "True"
min(str(not()))  →  "T"
ord(min(str(not())))  →  84
```

Two key operations let us reach any number:

- **3x multiplier**: `len(str(list(bytes(n))))` = `3n` exactly (4 parens)
- **Decrement**: `max(range(n))` = `n - 1` (2 parens)

With 3x and decrement, any number can be built in **base 3**: recursively build `ceil(n/3)`, triple it, then decrement 0-2 times. Base anchors (numbers constructible directly from builtins) serve as the recursion base cases.

Finally, wrap in `chr()` to get the character.

## Coverage

**100% of Unicode.** All 1,114,112 code points.

Max paren depth: 114 out of 200 limit.

| Code point | Depth |
|---|---|
| `a` (97) | 7 |
| ඞ (3,486) | 37 |
| BMP max (65,535) | 41 |
| 😀 (128,512) | 70 |
| Max Unicode (1,114,111) | 88 |

## Usage

```
$ python3 write_char_as_pyfuncs.py
Enter a character: a

Expression for 'a' (code point 97):
chr(max(range(ord(max(str(bytes()))))))

Verify: eval gives 'a'
```

## Files

- `anchors.py` — base anchors, operations, and `build_char()`
- `write_char_as_pyfuncs.py` — CLI wrapper
- `funcs_that_take_one_arg.txt` — exhaustive list of Python builtins that accept a single argument

## Operations

| Operation | Formula | Parens | Purpose |
|---|---|---|---|
| `len(str(list(bytes(n))))` | 3n | 4 | exact 3x multiplier |
| `len(str(bytes(n)))` | 4n + 3 | 3 | exact 4x multiplier |
| `len(ascii(str(bytes(n))))` | 5n + 5 | 4 | exact 5x multiplier |
| `sum(range(n))` | n(n-1)/2 | 2 | quadratic jump |
| `max(range(n))` | n - 1 | 2 | decrement |
