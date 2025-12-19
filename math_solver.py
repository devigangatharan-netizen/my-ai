import re

ALLOWED = re.compile(r'^[0-9+\-*/().\s]+$')

def solve_math(expr):
    expr = expr.replace("×", "*").replace("÷", "/")

    if not ALLOWED.match(expr):
        return None

    try:
        return eval(expr, {"__builtins__": {}}, {})
    except:
        return None
