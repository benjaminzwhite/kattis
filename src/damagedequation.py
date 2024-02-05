# Damaged Equation
# https://open.kattis.com/problems/damagedequation
# TAGS: brute force
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
WA on first submit due to not handling possibility of ZeroDivisionError when b or d == 0

If you use eval(), make sure you replace the chars to account for equality == and integer division //
"""
a, b, c, d = input().split()

OPS = "*+-/"
ok = False

for op1 in OPS:
    for op2 in OPS:
        expr = "{} {} {} = {} {} {}".format(a, op1, b, c, op2, d)
        try:
            if eval(expr.replace("=", "==").replace('/', '//')):
                print(expr)
                ok = True
        except ZeroDivisionError:
            continue

if not ok:
    print("problems ahead")