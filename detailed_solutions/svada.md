# Detailed solution for Kattis - Svada

[Problem statement on Kattis](https://open.kattis.com/problems/svada)

I thought that this was a cute binary search exercise with a nice theme.

## Tags

binary search

## Solution

For a given guess of `"first_monkey_time_limit"` (i.e time limit for first monkeys to do their job) you obtain a `total_time - first_monkey_time_limit = second_monkey_time_limit`

Then to do the binary search check, you want to make sure the number of coconuts is consistent on both sides, for this given guess of `first_monkey_time_limit`:

You calculate how many coconuts were produced on left side as follows:

```
first_coconuts = 0
for monkey in first_monkey:
    first_monkey_time_limit - monkey's A value (i.e. its initial search time)
    ---> this monkey has produced 1 coconut
    NOW IN REMAINING TIME, THAT MONKEY CAN PRODUCE time_remaining//monkey's B value more coconuts
```

Same argument for the "right side" monkeys, just changing `A,B` for `C,D`.

Finally, the binary search check is: if left_coconuts >= right, then you need **less time on the left**.

### Implementation notes

I was off-by-one on the 2 testcases: I'm not 100% sure I understand why, but it seems the binary search produces the lowest time at which you have **more coconuts on left side** than can be processed on right side.

So, with my binary search implementation at least, **in order to find the highest time at which you have equal or less coconuts on left side than can be processed**, you simply -1 the binary search result, i.e. `lo - 1` instead of `lo`.

## AC code

```python
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
```
