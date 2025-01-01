# Svada
# https://open.kattis.com/problems/svada
# TAGS: binary search
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/svada.md
"""
total_time = int(input())

fst = int(input())
first_monkeys = [] # meaningful variable names, good practice O_o
for _ in range(fst):
    a, b = map(int, input().split())
    first_monkeys.append((a, b))

snd = int(input())
second_monkeys = []
for _ in range(snd):
    c, d = map(int, input().split())
    second_monkeys.append((c, d))

lo, hi = 1, total_time
while lo < hi:
    first_monkey_time_limit = (lo + hi) // 2

    left_coconuts, right_coconuts = 0, 0
    for a, b in first_monkeys:
        if first_monkey_time_limit >= a:
            left_coconuts += 1 + (first_monkey_time_limit - a) // b

    for c, d in second_monkeys:
        second_monkey_time_limit = total_time - first_monkey_time_limit
        if second_monkey_time_limit >= c:
            right_coconuts += 1 + (second_monkey_time_limit - c) // d

    if left_coconuts > right_coconuts:
        hi = first_monkey_time_limit
    else:
        lo = first_monkey_time_limit + 1

print(lo - 1)