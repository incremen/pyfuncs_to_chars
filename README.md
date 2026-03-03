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

From 84, two operations let us reach other numbers:

- **Decrement**: `max(range(n))` = `n - 1` (2 parens per step)
- **Triangular jump**: `sum(range(k))` = `k * (k-1) / 2`

We also mine "anchors" — numbers we can construct cheaply from other builtins (e.g. `ord(max(str(bytes())))` = 98, because `str(bytes())` = `"b''"` and `max("b''"`) = `'b'`). To reach any target number, we find the nearest anchor above it and decrement down.

Finally, wrap in `chr()` to get the character.

## Usage

```
$ python3 write_char_as_pyfuncs.py
Enter a character: a

Expression for 'a' (code point 97):
chr(max(range(ord(max(str(bytes()))))))

Verify: eval gives 'a'
```

## Files

- `anchors.py` — base anchors, anchor expansion via triangular numbers, and `build_char()`
- `write_char_as_pyfuncs.py` — CLI wrapper
- `funcs_that_take_one_arg.txt` — exhaustive list of Python builtins that accept a single argument

## Constraints

- Python has a **200 nested parentheses limit**
- `chr()` wrapper costs 1 paren
- Each decrement (`max(range(...))`) costs **2 parens**
- Cheapest anchors cost 2-4 parens
- **Max ~98 decrements** per expression → anchors must be within ~98 of every target

## Coverage (current)

| Range | Coverage |
|---|---|
| 0-127 (ASCII) | 100% |
| 128-1000 | 100% |
| 1000-5000 | 100% |
| 5000-10000 | 98% |
| 10000-50000 | 63% |
| 50000-100000 | 38% |
| 100000-150000 | 29% |

Full ASCII + first 5000 code points fully covered. ~46% of 0-150k overall.

## Growing operations

Besides triangular (`sum(range(n))` = n*(n-1)/2), we discovered "multiplier" operations:

- `len(str(list(range(n))))` ≈ **4n** — list repr length
- `len(str(bytes(range(n))))` ≈ **2n** — bytes repr length (n ≤ 256)
- `len(str(bytearray(range(n))))` ≈ **2n** — bytearray repr length (n ≤ 256)

These cheaply produce numbers in the 100-550 range from base anchors (depth 8), which then feed into triangulars to cover the 5k-130k range.

## The remaining bottleneck

T(k+1) - T(k) = k. Once k > ~90 (our decrement budget), there's no integer between k and k+1 to produce an intermediate triangular. For example, T(510) = 129,795 and T(511) = 130,305 are 510 apart — no amount of anchors between 510 and 511 can fix this, since there are no integers there.

Covering the full 0-150k range would require a new operation that produces values directly in the 50k-150k range at low depth, without going through triangulars.

## Open questions

- Is there a single-arg builtin composition that grows faster than ~4x but slower than quadratic?
- Can we find operations that produce values in 50k+ directly, bypassing the T(k) gap problem?
