# Math Worksheet
# https://open.kattis.com/problems/mathworksheet
# TAGS: interpreter, string
# CP4: 6.2d, Output Formatting, H
# NOTES:
"""
Easy with Python eval() and string methods rjust().
Then it's just formatting - you need to print the exact lines between testcases etc.
"""
first_testcase = True

while True:
    n = int(input())
    if n == 0:
        break

    if not first_testcase:
        print()
    first_testcase = False # formatting stuff -.-
    
    vals = []
    for _ in range(n):
        vals.append(str(eval(input()))) # Python lol

    max_width = len(max(vals, key=len))

    # W_W_W_W..._W <= 50 INCLUSIVE
    # so have k*W's and k-1 spaces to fit
    # -> total len = k*W + k - 1 <= 50
    # k <= 51 / (W+1) is how many blocks to print per line
    k = 51 // (max_width + 1)
    i = 0
    while i < len(vals):
        l = vals[i : i + k]
        print(' '.join(x.rjust(max_width) for x in l))
        i += k