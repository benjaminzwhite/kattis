# Digital Speedometer
# https://open.kattis.com/problems/digitalspeedometer
# TAGS: interpreter, stack
# CP4: 0, Not In List Yet
# NOTES:
"""
A bit overranked, mainly reading comprehension - I just did line by line what is stated.

For the "lookbehind" stuff (the behavior between intervals):
I implemented it with a stack since you will never need to reuse popped values.
"""
from math import floor

tf = float(input())
tr = float(input())

stk = []
while True:
    try:
        s = float(input())
        i = floor(s)
        j = i + 1
        if s == 0: # these first 2 if elif: are the 2 special conditions that are just reading comprehension, AFTER the main i,j logic (bit confusing to implement out-of-order with reading text)
            print(0)
        elif j == 1:
            print(1)
        elif i <= s <= i + tf:
            print(i)
        elif i + tr <= s <= j:
            print(j)
        else:
            while stk and i + tf <= stk[-1] <= i + tr:
                stk.pop()
            ref = stk[-1]
            if ref < i + tr:
                print(i)
            else:
                print(j)
        stk.append(s)
    except EOFError:
        break