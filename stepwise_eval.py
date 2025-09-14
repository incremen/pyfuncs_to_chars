import re

def is_balanced(expr):
    stack = []
    for c in expr:
        if c == '(': stack.append(c)
        elif c == ')':
            if not stack: return False
            stack.pop()
    return not stack

def is_valid(expr):
    try:
        compile(expr, '<string>', 'eval')
        return True
    except Exception:
        return False

def find_paren_pairs(s):
    stack = []
    pairs = []
    for i, c in enumerate(s):
        if c == '(': stack.append(i)
        elif c == ')':
            if not stack:
                raise ValueError("Unbalanced parentheses")
            start = stack.pop()
            pairs.append((start, i))
    if stack:
        raise ValueError("Unbalanced parentheses")
    return pairs

def stepwise_bracket_eval(expr):
    s = expr
    print(f"Start: {s}")
    while True:
        lefts = [i for i, c in enumerate(s) if c == '(']
        rights = [i for i, c in enumerate(s) if c == ')']
        if not lefts or not rights or len(lefts) != len(rights):
            break
        n = len(lefts)
        pairs = [(lefts[i], rights[-(i+1)]) for i in range(n)]
        # Find the innermost (largest left, smallest right)
        innermost = max(pairs, key=lambda p: p[0])
        start, end = innermost
        subexpr = s[start:end+1]
        to_eval = s[start+1:end]
        try:
            val = eval(to_eval, {'__builtins__': __builtins__})
        except Exception as e:
            print(f"Error evaluating {to_eval!r}: {e}")
            
        print(f"Evaluating: {subexpr} = {val}")
        s = s[:start] + str(val) + s[end+1:]
        print(f"Now: {s}")
    print(f"Final eval: {s} = {eval(s, {'__builtins__': __builtins__})}")
    return

def main():
    # expr = input("Enter a Python expression to evaluate step by step: ")
    expr = "min(range(len(str(not()))))"
    try:
        stepwise_bracket_eval(expr)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
